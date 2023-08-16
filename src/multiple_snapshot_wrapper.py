import numpy as np
#from .profile_analyzer import ProfileAnalyzer #needed for pytest
#from profile_analyzer import ProfileAnalyzer #needed for jupyter
import profile_analyzer as pa

class MultipleSnapshotWrapper:

    def __init__(self, dir, field_strength, snapshots: list = None, negang_str: str = '-') -> None:
        assert type(snapshots) == list
        assert len(snapshots) > 0
        self.dir = dir
        self.snapshots = snapshots
        self.field_strength = field_strength
        self.negang_str = negang_str
        self.analyzers = []


    def run_multiple_analyzers(self):
        for snap in self.snapshots:
            temp = pa.ProfileAnalyzer(self.dir, self.field_strength, snap, self.negang_str)
            temp.run_analysis()
            self.analyzers.append(temp)


    def return_analyzers(self):
        return self.analyzers
    

    def num_snapshots(self):
        print(len(self.snapshots))
        return len(self.snapshots)
    
    
    def run_5250_fringe_analysis(self):
        for snap in self.snapshots:
            temp = pa.ProfileAnalyzer(self.dir, self.field_strength, snap, self.negang_str)
            temp.get_5250_fringe_line_frac()
            self.analyzers.append(temp)
            