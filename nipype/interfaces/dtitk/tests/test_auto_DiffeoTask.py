# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import DiffeoTask


def test_DiffeoTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fixed_file=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=0,
        ),
        ftol=dict(
            argstr='%s',
            exists=True,
            mandatory=True,
            position=5,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        legacy=dict(
            argstr='%s',
            exists=True,
            mandatory=True,
            position=3,
        ),
        mask=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=2,
        ),
        moving_file=dict(
            argstr='%s',
            exists=True,
            mandatory=False,
            position=1,
        ),
        n_iters=dict(
            argstr='%s',
            exists=True,
            mandatory=True,
            position=4,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = DiffeoTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DiffeoTask_outputs():
    output_map = dict(
        out_file=dict(),
        out_file_xfm=dict(),
    )
    outputs = DiffeoTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
