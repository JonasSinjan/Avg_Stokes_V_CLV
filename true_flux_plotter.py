import matplotlib.pyplot as plt
import numpy as np
from true_flux_analysers.profile_analyzer import ProfileAnalyzer
from true_flux_analysers.multiple_snapshot_wrapper import MultipleSnapshotWrapper

class TrueFluxPlotter:

    def __init__(self, ProfileWrapped: MultipleSnapshotWrapper) -> None:
        self.results = ProfileWrapped


    def get_x_plot(self) -> None:
        self.x_plot = self.results.mu_values
    
    
    def multiple_results_exist(self) -> bool:
        return len(self.results.snapshots) > 1
    
    
    def snapshot_exists(self, snapshot: int) -> bool:
       return snapshot in self.results.snapshots
    

    def get_snap_index(self, snapshot: int) -> None:
        self.snap_index = self.results.snapshots.index(snapshot)
    

    def get_temp_comb_curves(self) -> None:
        self.temp_samp = self.results.analyzer[self.snap_index].comb_normed_signed_amp
        self.temp_usamp = self.results.analyzer[self.snap_index].comb_normed_unsigned_amp
        self.temp_sarea = self.results.analyzer[self.snap_index].comb_normed_signed_area
        self.temp_usarea = self.results.analyzer[self.snap_index].comb_normed_unsigned_area


    def get_snapshot_comb_results(self, snapshot: int) -> None:
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_comb_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_comb_single_snapshot(self, snapshot: int) -> None:
        self.get_snapshot_comb_results(self,snapshot)
        self.get_x_plot()

        plt.figure(figsize = (8,6))
        plt.plot(self.x_plot, self.temp_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        plt.plot(self.x_plot, self.temp_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        plt.plot(self.x_plot, self.temp_sarea, marker = "o", markersize = 3, label = "Signed Area")
        plt.plot(self.x_plot, self.temp_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        plt.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        plt.tick_params(bottom=True,top=True,left=True,right=True)
        plt.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        plt.axhline(y = 0, color = "black")
        plt.legend(loc="upper right")
        plt.xlabel(r"$\mu=cos(\theta)$")
        plt.ylabel("(Area or Amp) (normalised) / $\mu$")
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (pos+neg) (normalised) {self.field_strength}G / $\mu$")
        plt.show()
    
    def get_temp_sep_curves(self) -> None:
        self.temp_pos_samp = self.results.analyzer[self.snap_index].pos_normed_signed_amp
        self.temp_pos_usamp = self.results.analyzer[self.snap_index].pos_normed_unsigned_amp
        self.temp_pos_sarea = self.results.analyzer[self.snap_index].pos_normed_signed_area
        self.temp_pos_usarea = self.results.analyzer[self.snap_index].pos_normed_unsigned_area

        self.temp_neg_samp = self.results.analyzer[self.snap_index].neg_normed_signed_amp
        self.temp_neg_usamp = self.results.analyzer[self.snap_index].neg_normed_unsigned_amp
        self.temp_neg_sarea = self.results.analyzer[self.snap_index].neg_normed_signed_area
        self.temp_neg_usarea = self.results.analyzer[self.snap_index].neg_normed_unsigned_area


    def get_snapshot_sep_results(self, snapshot: int) -> None:
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_sep_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_pos_neg_single_snapshot(self, snapshot: int) -> None:
        self.get_snapshot_sep_results(self,snapshot)
        self.get_x_plot()

        plt.figure(figsize = (16,6))
        plt.subplot(1,2,1)
        plt.plot(self.x_plot, self.temp_pos_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        plt.plot(self.x_plot, self.temp_pos_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        plt.plot(self.x_plot, self.temp_pos_sarea, marker = "o", markersize = 3, label = "Signed Area")
        plt.plot(self.x_plot, self.temp_pos_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        plt.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        plt.tick_params(bottom=True,top=True,left=True,right=True)
        plt.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        plt.axhline(y = 0, color = "black")
        plt.legend(loc="upper right")
        plt.xlabel(r"$\mu=cos(\theta)$")
        plt.ylabel("(Area or Amp) (normalised) / $\mu$")
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (pos) (normalised) {self.field_strength}G / $\mu$")

        plt.subplot(1,2,2)
        plt.plot(self.x_plot, self.temp_neg_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        plt.plot(self.x_plot, self.temp_neg_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        plt.plot(self.x_plot, self.temp_neg_sarea, marker = "o", markersize = 3, label = "Signed Area")
        plt.plot(self.x_plot, self.temp_neg_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        plt.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        plt.tick_params(bottom=True,top=True,left=True,right=True)
        plt.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        plt.axhline(y = 0, color = "black")
        plt.legend(loc="upper right")
        plt.xlabel(r"$\mu=cos(\theta)$")
        plt.ylabel("(Area or Amp) (normalised) / $\mu$")
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (neg) (normalised) {self.field_strength}G / $\mu$")

        plt.show()


    def get_snap_indices(self, snapshots) -> None:
        self.snap_indices = []
        for i in snapshots:
            self.snap_indices.append(self.results.snapshots.index(i))
        assert len(self.snap_indices) > 0, "No snapshots have been selected/found"


    def avg_curves(self) -> None:
        self.temp_usarea = np.mean([self.results.analyzer[i].comb_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.temp_usamp = np.mean([self.results.analyzer[i].comb_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.temp_sarea = np.mean([self.results.analyzer[i].comb_normed_signed_area for i in self.snap_indices], axis = 0)
        self.temp_samp = np.mean([self.results.analyzer[i].comb_normed_signed_amp for i in self.snap_indices], axis = 0)


    def std_curves(self) -> None:
        self.std_usarea = np.std([self.results.analyzer[i].comb_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.std_usamp = np.std([self.results.analyzer[i].comb_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.std_sarea = np.std([self.results.analyzer[i].comb_normed_signed_area for i in self.snap_indices], axis = 0)
        self.std_samp = np.std([self.results.analyzer[i].comb_normed_signed_amp for i in self.snap_indices], axis = 0)
        

    def get_avg_std_of_curves(self, snapshots: list) -> None:
        if self.all_snapshots_exist(snapshots):
            self.get_snap_indices(snapshots)
            self.avg_curves()
            self.std_curves
        else:
            print("Snapshots do not exist in", self.results.snapshots)


    def plot_comb_multiple_snapshots(self, snapshots: list = None) -> None:
        self.get_avg_std_of_curves(snapshots)
        self.get_x_plot()

        plt.figure(figsize = (8,6))
        plt.subplot(1,2,1)
        plt.plot(self.x_plot, self.temp_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        plt.plot(self.x_plot, self.temp_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        plt.plot(self.x_plot, self.temp_sarea, marker = "o", markersize = 3, label = "Signed Area")
        plt.plot(self.x_plot, self.temp_samp, marker = "o", markersize = 3, label = "Signed Amp")     

        plt.fill_between(self.x_plot, self.temp_usarea-self.std_usarea, self.temp_usarea+self.std_usarea, color = 'blue', alpha = 0.2)
        plt.fill_between(self.x_plot, self.temp_usamp-self.std_usamp, self.temp_usamp+self.std_usamp, color = 'orange', alpha = 0.2)
        plt.fill_between(self.x_plot, self.temp_sarea-self.std_sarea, self.temp_sarea+self.std_sarea, color = 'green', alpha = 0.2)
        plt.fill_between(self.x_plot, self.temp_samp-self.std_samp, self.temp_samp+self.std_samp, color = 'red', alpha = 0.2)   

        plt.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        plt.tick_params(bottom=True,top=True,left=True,right=True)
        plt.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        plt.axhline(y = 0, color = "black")
        plt.legend(loc="upper right")
        plt.xlabel(r"$\mu=cos(\theta)$")
        plt.ylabel("(Area or Amp) (normalised) / $\mu$")
        plt.title(f"(Num Snapshot(s): {len(snapshots)} Stokes V Signal (pos+neg) (normalised) {self.field_strength}G / $\mu$")

        plt.show()



        """
        if self.multiple_results_exist():
            self.get_std_curves()
            plt.fill_between(self.x_plot, self.avg_usarea-self.std_usarea, self.avg_usarea+self.std_usarea, color = 'blue', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_usamp-self.std_usamp, self.avg_usamp+self.std_usamp, color = 'orange', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_sarea-self.std_sarea, self.avg_sarea+self.std_sarea, color = 'green', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_samp-self.std_samp, self.avg_samp+self.std_samp, color = 'red', alpha = 0.2)"""