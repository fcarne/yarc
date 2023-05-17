from typing import Any

import importlib

from antlr3 import Parser

from yarc.dsl.v3.handler.handler import Handler


def import_guard() -> bool:
    try:
        spec = importlib.util.find_spec("omni.replicator.core")
        return spec is not None
    except (ImportError, ModuleNotFoundError):
        return False


# TODO: edit
DIRECTIVE_ACCEPTED_PARAMS = {
    "group": {"items", "semantics"},
    "light": {
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
        "count",
        "name",
    },
    "material_omnipbr": {
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
        "count",
    },
    "camera": {
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
        "count",
        "parent",
        "name",
    },
    "stereo_camera": {
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
        "count",
        "name",
    },
    "disk": {
        "position",
        "scale",
        "pivot",
        "rotation",
        "look_at",
        "look_at_up_axis",
        "semantics",
        "material",
        "visible",
        "count",
        "name",
    },
    "from_usd": {"usd", "semantics", "count"},
    "get": {"path_pattern", "path_pattern_exclusion", "semantics"},
    "scatter_2d": {
        "surface_prims",
        "seed",
        "offset",
        "check_for_collisions",
        "input_prims",
    },
    "scatter_3d": {
        "volume_prims",
        "resolution_scaling",
        "check_for_collisions",
        "seed",
        "input_prims",
    },
    "collider": {"approximation_shape", "contact_offset", "rest_offset", "input_prims"},
    "drive_properties": {"stiffness", "damping", "input_prims"},
    "mass": {
        "mass",
        "density",
        "center_of_mass",
        "diagonal_inertia",
        "principal_axes",
        "input_prims",
    },
    "physics_material": {
        "static_friction",
        "dynamic_friction",
        "restitution",
        "input_prims",
    },
    "rigid_body": {
        "velocity",
        "angular_velocity",
        "contact_offset",
        "rest_offset",
        "input_prims",
    },
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

    def special_setting_to_str(self, setting: str, value: Any) -> str:
        if setting in self.carb_mapping:
            return self.parser.templateLib.getInstanceOf(
                "setting",
                attributes={
                    "setting": setting,
                    "value": str(value),
                },
            )
        return super().special_setting_to_str(setting, value)
