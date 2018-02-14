# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..tracking import FilterTracks


def test_FilterTracks_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        debug=dict(
            argstr='-debug',
            position=1,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        exclude_file=dict(
            argstr='-exclude %s',
            xor=['exclude_file', 'exclude_spec'],
        ),
        exclude_spec=dict(
            argstr='-exclude %s',
            position=2,
            sep=',',
            units='mm',
            xor=['exclude_file', 'exclude_spec'],
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        include_file=dict(
            argstr='-include %s',
            xor=['include_file', 'include_spec'],
        ),
        include_spec=dict(
            argstr='-include %s',
            position=2,
            sep=',',
            units='mm',
            xor=['include_file', 'include_spec'],
        ),
        invert=dict(argstr='-invert', ),
        minimum_tract_length=dict(
            argstr='-minlength %s',
            units='mm',
        ),
        no_mask_interpolation=dict(argstr='-nomaskinterp', ),
        out_file=dict(
            argstr='%s',
            hash_files=False,
            name_source=['in_file'],
            name_template='%s_filt',
            position=-1,
        ),
        quiet=dict(
            argstr='-quiet',
            position=1,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = FilterTracks.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FilterTracks_outputs():
    output_map = dict(out_file=dict(), )
    outputs = FilterTracks.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
