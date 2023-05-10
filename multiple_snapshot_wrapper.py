import numpy as np
from true_flux_analysers.profile_analyzer import ProfileAnalyzer

class MultipleSnapshotWrapper:

    def __init__(self, field_strength, snapshots) -> None:
        assert type(snapshots) == list
        assert len(snapshots) > 1
        self.snapshots = snapshots
        self.field_strength = field_strength


    def run_multiple_snapshot_analyzers(self):
        self.analyzers = []
        for snap in self.snapshots:
            self.analyzers.append(ProfileAnalyzer(self.field_strength, snap).run_analysis())


    def return_analyzers(self):
        return self.analyzers