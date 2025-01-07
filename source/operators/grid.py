from bpy.types import Operator


class ToGrid(Operator):
    def execute(self, context):
        dk = context.scene.dk_tools

        value = dk.grid_start
        pad = dk.grid_pad
        count = dk.grid_count
        fn = dk.grid_fn  # TODO: search for callable in realtime stack

        x_start = (pad / 2) * (count / 4) * -1
        offset = (x_start, (pad / 2) * (count / 4))
        i = 0
        while i < count and value <= dk.grid_end:
            fn_val(value, fn_args, fn_kwargs)
            fn(*fn_args, **fn_kwargs)
            value += dk.grid_step
            x, y = offset
            x += pad
            i += 1
            if i % 4 == 0 and i > 0:
                x = x_start
                y -= pad
            offset = (x, y)
