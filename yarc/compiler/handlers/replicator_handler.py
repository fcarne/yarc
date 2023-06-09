from typing import Any, Optional

import ast
import time

from antlr3 import Parser, Token

from yarc.compiler.handlers.formatters.error_formatter import ErrorType
from yarc.compiler.handlers.formatters.warning_formatter import WarningType
from yarc.compiler.handlers.handler import Attribute, Handler, Parameter

PRIMS = {
    "Plane": "plane",
    "Cube": "cube",
    "Cone": "cone",
    "Torus": "torus",
    "Sphere": "sphere",
    "Cylinder": "cylinder",
    "Disk": "disk",
    "Light": "light",
    "Camera": "camera",
    "Stereo Camera": "stereo_camera",
    "Material": "material_omnipbr",
}

DISTRIBUTIONS = {
    "Uniform": "uniform",
    "Normal": "normal",
    "Choice": "choice",
    "Sequence": "sequence",
    "LogUniform": "log_uniform",
    "Combine": "combine",
}

PARAMS = {
    "translate": "position",
    "rotate": "rotation",
    "scale": "scale",
    "semantics": "semantics",
    "visible": "visible",
    "size": "size",
    "look_at": "look_at",
    "up_axis": "look_at_up_axis",
    "pivot": "pivot",
    "material": "material",
    "scatter_2d": "scatter_2d",
    "scatter_3d": "scatter_3d",
    "rotate_around": "rotate_around",
    "move_to_camera": "pose_camera_relative",
    "collider": "collider",
    "kinematics": "rigid_body",
    "rigid_body": "mass",
    "physics_material": "physics_material",
}

GET_TARGETS = {
    "Prims": "prims",
    "Camera": "camera",
    "Curve": "curve",
    "Geomsubset": "geomsubset",
    "Graph": "graph",
    "Light": "light",
    "Listener": "listener",
    "Material": "material",
    "Mesh": "mesh",
    "Physics": "physics",
    "Renderproduct": "renderproduct",
    "Rendervar": "rendervar",
    "Scope": "scope",
    "Shader": "shader",
    "Shape": "shape",
    "Sound": "sound",
    "Xform": "xform",
}

ACCEPTED_PARAMS: dict[str, set[str] | dict[str, set[str]]] = {
    "EDIT": set(),
    "GROUP": set(),
    "LIGHT": {
        "position",
        "scale",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "type",
        "color",
        "intensity",
        "exposure",
        "temperature",
        "texture",
    },
    "MATERIAL": {
        "diffuse",
        "diffuse_texture",
        "roughness",
        "roughness_texture",
        "metallic",
        "metallic_texture",
        "specular",
        "emissive_color",
        "emissive_texture",
        "emissive_intensity",
        "project_uvw",
        "semantics",
    },
    "CAMERA": {
        "position",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "focal_length",
        "focus_distance",
        "f_stop",
        "horizontal_aperture",
        "horizontal_aperture_offset",
        "vertical_aperture_offset",
        "clipping_range",
        "projection_type",
        "fisheye_nominal_width",
        "fisheye_nominal_height",
        "fisheye_optical_centre_x",
        "fisheye_optical_centre_y",
        "fisheye_max_fov",
        "fisheye_polynomial_a",
        "fisheye_polynomial_b",
        "fisheye_polynomial_c",
        "fisheye_polynomial_d",
        "fisheye_polynomial_e",
    },
    "STEREO": {
        "stereo_baseline",
        "position",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "focal_length",
        "focus_distance",
        "f_stop",
        "horizontal_aperture",
        "horizontal_aperture_offset",
        "vertical_aperture_offset",
        "clipping_range",
        "projection_type",
        "fisheye_nominal_width",
        "fisheye_nominal_height",
        "fisheye_optical_centre_x",
        "fisheye_optical_centre_y",
        "fisheye_max_fov",
        "fisheye_polynomial_a",
        "fisheye_polynomial_b",
        "fisheye_polynomial_c",
        "fisheye_polynomial_d",
        "fisheye_polynomial_e",
    },
    "SHAPE": {
        "position",
        "scale",
        "pivot",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "semantics",
        "material",
        "visible",
    },
    "FROM": set(),
    "GET": {
        "exclude",
        "include_semantics",
        "exclude_semantics",
        "cache_result",
    },
    "INSTANTIATE": {"weights", "mode", "with_replacements", "seed", "use_cache"},
    "SCATTER": {
        "scatter_2d": {
            "seed",
            "offset",
            "check_for_collisions",
        },
        "scatter_3d": {
            "resolution_scaling",
            "check_for_collisions",
            "seed",
        },
    },
    "PHYSICS": {
        "collider": {"approximation_shape", "contact_offset", "rest_offset"},
        "rigid_body": {
            "mass",
            "density",
            "center_of_mass",
            "diagonal_inertia",
            "principal_axes",
        },
        "physics_material": {
            "static_friction",
            "dynamic_friction",
            "restitution",
        },
        "kinematics": {
            "velocity",
            "angular_velocity",
            "contact_offset",
            "rest_offset",
        },
    },
    "ROT_AROUND": {
        "radius",
        "number_of_positions",
        "current_position",
        "relative_offset",
        "look_at_up_axis",
    },
    "MOVE_TO_CAM": {"distance", "horizontal_location", "vertical_location"},
}

INCOMPATIBLE_ATTRS = [
    {"translate", "scatter_2d", "scatter_3d", "move_to_camera", "rotate_around"},
    {"rotate", "look_at", "rotate_around"},
    {"scale", "size"},
]

SUPPORTED_WRITERS = {
    "BasicWriter",
    "KittiWriter",
    "DemoWriter",
    "DOPEWriter",
    "YCBVideoWriter",
}


class OmniReplicatorHandler(Handler):
    def __init__(
        self,
        parser: Parser,
        warnings: bool = False,
        num_scenes: Optional[int] = None,
        mount: Optional[str] = None,
    ):
        super().__init__(parser, warnings, num_scenes, mount)

        self.default_settings.update(
            {
                "render_mode": "RayTracedLighting",
                "rtx_antialiasing": "FXAA",
                "pathtracing_samples_per_pixel": 64,
            }
        )

        self.carb_mapping = {
            "render_mode": "/rtx/rendermode",
            "rtx_antialiasing": "/rtx/post/aa/op",
            "pathtracing_samples_per_pixel": "/rtx/pathtracing/totalSpp",
        }

        self.mapping = PRIMS | DISTRIBUTIONS | PARAMS | GET_TARGETS

    def special_setting_to_str(self, setting: Token | str, value: Any) -> Optional[str]:
        setting = setting.text if isinstance(setting, Token) else str(setting)
        if setting in self.carb_mapping:
            return str(
                self.parser.templateLib.getInstanceOf(
                    "setting",
                    attributes={
                        "setting": setting,
                        "value": str(value),
                    },
                )
            )
        return super().special_setting_to_str(setting, value)

    def parse_snippet(self, snippet: Token) -> str:
        code: str = snippet.text.lstrip("{{").rstrip("}}").strip()

        try:
            compile(code, "<string>", "exec")
        except SyntaxError as e:
            msg = f"{ErrorType.SNIPPET_ERROR.default_msg} -> {e}"
            self.handle_error(type=ErrorType.SNIPPET_ERROR, msg=msg, tk=snippet)

        tree = ast.parse(code)
        names = {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
        }
        for name in names:
            self.symbol_stack.define(name, object, used=True)

        return code

    def get_params(
        self,
        token: Token,
        attrs: list[Attribute] | None,
        warnings: bool = False,
        **kwargs: Any,
    ) -> list[Parameter]:
        if attrs is None:
            return []

        accepted_params = self.__get_accepted_params(token)
        params = [
            Parameter(self.__rewrite_param(token, attr.name), attr.value)
            for attr in attrs
            if attr.name in accepted_params
        ]
        for name, value in kwargs.items():
            if value is not None:
                params.append(Parameter(self.__rewrite_param(token, name), value))

        if self.show_warnings and warnings:
            unknown_params = [
                attr.name for attr in attrs if attr.name not in accepted_params
            ]
            for param in unknown_params:
                self.handle_warning(
                    type=WarningType.UNKNOWN_PARAMETER,
                    tk=token,
                    param=param,
                    command=self.__get_command(token),
                    accepted_params=accepted_params,
                )

        return params

    def get_attrs(self, token: Token, attrs: list[Attribute] | None) -> list[str]:
        if attrs is None:
            return []

        accepted_params = self.__get_accepted_params(token)

        if self.show_warnings:
            attrs_set = [attr.name for attr in attrs]
            for incompatible_set in INCOMPATIBLE_ATTRS:
                common_attrs = incompatible_set.intersection(attrs_set)
                if len(common_attrs) > 1:
                    last_set = max(common_attrs, key=lambda attr: attrs_set.index(attr))
                    others = common_attrs
                    others.remove(last_set)

                    self.handle_warning(
                        type=WarningType.OVERWRITTEN_ATTRIBUTE,
                        tk=token,
                        last=last_set,
                        others=common_attrs,
                    )

        return [attr.st for attr in attrs if attr.name not in accepted_params]

    def __get_accepted_params(self, token: Token) -> set[str]:
        params = ACCEPTED_PARAMS[token.typeName]
        return params if isinstance(params, set) else params[token.text]

    def __rewrite_param(self, token: Token, param: str) -> str:
        match (token.typeName, param):
            case ("LIGHT", "type"):
                return "light_type"
            case ("GET", "exclude"):
                return "path_pattern_exclusion"
            case ("GET", "include_semantics"):
                return "semantics"
            case ("GET", "exclude_semantics"):
                return "semantics_exclusion"
            case _:
                return param

    def __get_command(self, token: Token) -> str:
        from yarc.compiler.YarcLexer import CAMERA, FROM, LIGHT, MATERIAL, SHAPE, STEREO

        type = token.type

        if type == STEREO:
            return "create stereo camera"
        elif type in [SHAPE, LIGHT, CAMERA, FROM, MATERIAL]:
            return f"create {token.text}"

        return str(token.text)

    def get_behaviors(self, attrs: list[Attribute] | None) -> list[str]:
        if attrs is None:
            return []
        return [attr.st for attr in attrs if attr.name == Handler.BEHAVIOR]

    def map(self, *tokens: Token) -> str:
        tokens_text = [str(token.text) for token in tokens if token is not None]

        return "_".join([self.mapping.get(t, t.lower()) for t in tokens_text])

    def check_writer(self, writer: Token, params: list[Parameter]) -> None:
        if writer.text not in SUPPORTED_WRITERS:
            self.handle_error(
                type=ErrorType.WRITER_ERROR, writer=writer.text, tk=writer
            )

        names = [param.name for param in params]
        output_dir_param = "output_dir"
        if output_dir_param not in names:
            default = self.expand_string(
                f"'*/{writer.text.lower()}_{int(time.time() * 1000)}'"
            )
            params.append(Parameter(output_dir_param, default))

            if self.show_warnings:
                self.handle_warning(
                    WarningType.MISSING_WRITER_PARAMETER,
                    param=output_dir_param,
                    writer=writer.text,
                    default=default,
                )

    def check_target(self, tk: Token) -> None:
        target = tk.text

        if self.show_warnings and target not in GET_TARGETS:
            self.handle_warning(
                WarningType.UNSUPPORTED_GET_TARGET,
                tk,
                target=target,
                supported_targets=GET_TARGETS.keys(),
            )
