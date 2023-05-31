import numpy as np
#from .profile_analyzer import ProfileAnalyzer #needed for pytest
#from profile_analyzer import ProfileAnalyzer #needed for jupyter
import profile_analyzer as pa

class MultipleSnapshotWrapper:

    def __init__(self, field_strength, snapshots: list = None, negang_str: str = '-', sqrt4pi: str = '') -> None:
        assert type(snapshots) == list
        assert len(snapshots) > 0
        self.snapshots = snapshots
        self.field_strength = field_strength
        self.negang_str = negang_str
        self.analyzers = []
        self.sqrt4pi = sqrt4pi


    def run_multiple_analyzers(self):
        for snap in self.snapshots:
            temp = pa.ProfileAnalyzer(self.field_strength, snap, self.negang_str, self.sqrt4pi)
            temp.run_analysis()
            self.analyzers.append(temp)


    def return_analyzers(self):
        return self.analyzers
    

    def num_snapshots(self):
        print(len(self.snapshots))
        return len(self.snapshots)