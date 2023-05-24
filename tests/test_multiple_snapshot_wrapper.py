import pytest
from ..src.multiple_snapshot_wrapper import MultipleSnapshotWrapper
import numpy as np
import numpy.testing as npt

def test_mult_init():
    multi_test = MultipleSnapshotWrapper(30, [200000, 201000])
    assert multi_test.field_strength == 30
    assert multi_test.snapshots == [200000, 201000]
    assert multi_test.negang_str == '-'
    assert multi_test.num_snapshots() == 2
    

def test_mult_run():
    multi_test = MultipleSnapshotWrapper(30, [200000, 201000])
    multi_test.run_multiple_analyzers()
    assert len(multi_test.analyzers) == 2
    assert multi_test.analyzers[0].field_strength == 30
    assert multi_test.analyzers[0].snapshot == 200000
    assert multi_test.analyzers[1].field_strength == 30
    assert multi_test.analyzers[1].snapshot == 201000
    assert multi_test.return_analyzers() == multi_test.analyzers
    assert multi_test.analyzers[0].mu_values == [0.0486,0.1007,0.1493,0.2014,0.25,0.2986,0.3993,0.5,0.6007,0.7014,0.7986,0.8993,1.0]
    npt.assert_array_almost_equal(multi_test.analyzers[0].comb_normed_signed_amp, np.array([2.18346201, 1.38126857, 1.20914884, 1.11256635, 1.05451223, 1.01931797,
 0.97527902, 0.97874004, 0.98816226, 1.00424772, 1.01614571, 1.01435845,
 1.        ]))

