from typing import Any, Union

import ast
import importlib

from antlr3 import Parser, Token

from yarc.dsl.v3.handler.handler import Attribute, Handler, Parameter


def import_guard() -> bool:
    try:
        spec = importlib.util.find_spec("omni.replicator.core")
        return spec is not None
    except (ImportError, ModuleNotFoundError):
        return False


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

ACCEPTED_PARAMS = {
    "EDIT": set(),
    "GROUP": set(),
    "LIGHT": {
        "position",
        "scale",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "light_type",
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
        "path_pattern_exclusion",
        "semantics",
        "path_pattern_exclusion",
        "semantics",
        "semantics_exclusion",
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
    "ROT_AROUND": {...},
}


class OmniReplicatorHandler(Handler):
    def __init__(self, parser: Parser):
        super().__init__(parser)

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

        self._map_settings()

        self.mapping = PRIMS | DISTRIBUTIONS | PARAMS | GET_TARGETS

    def special_setting_to_str(self, setting: str, value: Any) -> str:
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
        code = snippet.text.lstrip("{{").rstrip("}}").strip()

        try:
            compile(code, "<string>", "exec")
        except SyntaxError as e:
            print(f"Syntax error: {e}")
            # TODO: add error

        tree = ast.parse(code)
        names = {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
        }
        for name in names:
            self.symbol_stack.define(name, Any, used=True)

        return code

    def get_params(
        self, token: Token, attrs: list[Attribute], warnings=False, **kwargs
    ) -> list[Parameter]:
        if attrs is None:
            return []

        accepted_params = self.__get_accepted_params(token)
        params = [
            Parameter(attr.name, attr.value)
            for attr in attrs
            if attr.name in accepted_params
        ]
        for key, value in kwargs.items():
            params.append(Parameter(name=key, value=value))

        if warnings:
            [attr.name for attr in attrs if attr.name not in accepted_params]
            # TODO: add warning + most_similar
        return params

    def get_attrs(self, token: Token, attrs: list[Attribute]) -> list[str]:
        if attrs is None:
            return []

        accepted_params = self.__get_accepted_params(token)
        return [attr.st for attr in attrs if attr.name not in accepted_params]

    def __get_accepted_params(self, token: Token) -> set[str]:
        params = ACCEPTED_PARAMS[token.typeName]
        return params if isinstance(params, set) else params[token.text]

    def __rewrite_value(self, value: Any) -> Any:
        if isinstance(value, str) and value.contains("Gf.Vec"):
            # add
            pass

        return value

    def get_behaviors(self, attrs: list[Attribute]) -> list[str]:
        if attrs is None:
            return []
        return [attr.st for attr in attrs if attr.name == Handler.BEHAVIOR]

    def map(self, *tokens: list[Union[Token, str]]) -> str:
        tokens = [
            token.text if isinstance(token, Token) else str(token.st)
            for token in tokens
            if token is not None
        ]

        return "_".join([self.mapping.get(t, t.lower()) for t in tokens])

    def check_writer_params(self, writer_params: list[Parameter]) -> None:
        params = [param.name for param in writer_params]

        if "output_dir" not in params:
            # TODO: raise Error or default
            pass

    def check_target(self, target: Union[Token, str]) -> None:
        target = target.text if isinstance(target, Token) else str(target.st)
        if target not in GET_TARGETS:
            # TODO: add error / warning
            pass
