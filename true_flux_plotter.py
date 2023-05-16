import matplotlib.pyplot as plt
import numpy as np
from multiple_snapshot_wrapper import MultipleSnapshotWrapper

class TrueFluxPlotter:

    def __init__(self, ProfileWrapped: MultipleSnapshotWrapper) -> None:
        self.results = ProfileWrapped


    def get_x_plot(self) -> None:
        self.x_plot = self.results.analyzers[0].mu_values
    
    
    def multiple_results_exist(self) -> bool:
        return len(self.results.snapshots) > 1
    
    
    def snapshot_exists(self, snapshot: int) -> bool:
       return snapshot in self.results.snapshots
    

    def get_snap_index(self, snapshot: int) -> None:
        self.snap_index = self.results.snapshots.index(snapshot)
    

    def get_temp_comb_curves(self) -> None:
        self.temp_samp = self.results.analyzers[self.snap_index].comb_normed_signed_amp
        self.temp_usamp = self.results.analyzers[self.snap_index].comb_normed_unsigned_amp
        self.temp_sarea = self.results.analyzers[self.snap_index].comb_normed_signed_area
        self.temp_usarea = self.results.analyzers[self.snap_index].comb_normed_unsigned_area


    def get_snapshot_comb_results(self, snapshot: int) -> None:
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_comb_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_comb_single_snapshot(self, snapshot: int) -> None:
        self.get_snapshot_comb_results(self,snapshot)
        self.get_x_plot()

        _, ax = plt.subplots(figsize = (8,6))
        ax.plot(self.x_plot, self.temp_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        ax.plot(self.x_plot, self.temp_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        ax.plot(self.x_plot, self.temp_sarea, marker = "o", markersize = 3, label = "Signed Area")
        ax.plot(self.x_plot, self.temp_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        ax.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        ax.tick_params(bottom=True,top=True,left=True,right=True)
        ax.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        ax.axhline(y = 0, color = "black")
        ax.set_legend(loc="upper right")
        ax.set_xlabel(r"$\mu=cos(\theta)$")
        ax.set_ylabel("(Area or Amp) (normalised) / $\mu$")
        ax.set_title(f"(Snapshot: {snapshot} Stokes V Signal (pos+neg) (normalised) {self.results.field_strength}G / $\mu$")
        return ax
    
    def get_temp_sep_curves(self) -> None:
        self.temp_pos_samp = self.results.analyzers[self.snap_index].pos_normed_signed_amp
        self.temp_pos_usamp = self.results.analyzers[self.snap_index].pos_normed_unsigned_amp
        self.temp_pos_sarea = self.results.analyzers[self.snap_index].pos_normed_signed_area
        self.temp_pos_usarea = self.results.analyzers[self.snap_index].pos_normed_unsigned_area

        self.temp_neg_samp = self.results.analyzers[self.snap_index].neg_normed_signed_amp
        self.temp_neg_usamp = self.results.analyzers[self.snap_index].neg_normed_unsigned_amp
        self.temp_neg_sarea = self.results.analyzers[self.snap_index].neg_normed_signed_area
        self.temp_neg_usarea = self.results.analyzers[self.snap_index].neg_normed_unsigned_area


    def get_snapshot_sep_results(self, snapshot: int) -> None:
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_sep_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_pos_neg_single_snapshot(self, snapshot: int) -> None:
        self.get_snapshot_sep_results(self,snapshot)
        self.get_x_plot()

        _, axarr = plt.subplots(1,2,figsize = (16,6))
        axarr[0].plot(self.x_plot, self.temp_pos_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        axarr[0].plot(self.x_plot, self.temp_pos_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        axarr[0].plot(self.x_plot, self.temp_pos_sarea, marker = "o", markersize = 3, label = "Signed Area")
        axarr[0].plot(self.x_plot, self.temp_pos_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        axarr[0].plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        axarr[0].tick_params(bottom=True,top=True,left=True,right=True)
        axarr[0].tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        axarr[0].axhline(y = 0, color = "black")
        axarr[0].legend(loc="upper right")
        axarr[0].set_xlabel(r"$\mu=cos(\theta)$")
        axarr[0].set_ylabel("(Area or Amp) (normalised) / $\mu$")
        axarr[0].set_title(f"(Snapshot: {snapshot} Stokes V Signal (pos) (normalised) {self.results.field_strength}G / $\mu$")

        axarr[1].plot(self.x_plot, self.temp_neg_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        axarr[1].plot(self.x_plot, self.temp_neg_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        axarr[1].plot(self.x_plot, self.temp_neg_sarea, marker = "o", markersize = 3, label = "Signed Area")
        axarr[1].plot(self.x_plot, self.temp_neg_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        axarr[1].plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        axarr[1].tick_params(bottom=True,top=True,left=True,right=True)
        axarr[1].tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        axarr[1].axhline(y = 0, color = "black")
        axarr[1].legend(loc="upper right")
        axarr[1].set_xlabel(r"$\mu=cos(\theta)$")
        axarr[1].set_ylabel("(Area or Amp) (normalised) / $\mu$")
        axarr[1].set_title(f"(Snapshot: {snapshot} Stokes V Signal (neg) (normalised) {self.results.field_strength}G / $\mu$")
        return axarr


    def get_snap_indices(self, snapshots) -> None:
        self.snap_indices = []
        for i in snapshots:
            self.snap_indices.append(self.results.snapshots.index(i))
        assert len(self.snap_indices) > 0, "No snapshots have been selected/found"


    def avg_curves(self) -> None:
        self.temp_usarea = np.mean([self.results.analyzers[i].comb_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.temp_usamp = np.mean([self.results.analyzers[i].comb_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.temp_sarea = np.mean([self.results.analyzers[i].comb_normed_signed_area for i in self.snap_indices], axis = 0)
        self.temp_samp = np.mean([self.results.analyzers[i].comb_normed_signed_amp for i in self.snap_indices], axis = 0)


    def std_curves(self) -> None:
        self.std_usarea = np.std([self.results.analyzers[i].comb_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.std_usamp = np.std([self.results.analyzers[i].comb_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.std_sarea = np.std([self.results.analyzers[i].comb_normed_signed_area for i in self.snap_indices], axis = 0)
        self.std_samp = np.std([self.results.analyzers[i].comb_normed_signed_amp for i in self.snap_indices], axis = 0)
        

    def all_snapshots_exist(self, snapshots: list) -> bool:
        return all(x in self.results.snapshots for x in snapshots)
    

    def get_avg_std_of_curves(self, snapshots: list) -> None:
        if self.all_snapshots_exist(snapshots):
            self.get_snap_indices(snapshots)
            self.avg_curves()
            self.std_curves()
        else:
            print("Snapshots do not exist in", self.results.snapshots)


    def plot_comb_multiple_snapshots(self, snapshots: list = None, ) -> plt.axes:
        if snapshots == None:
            snapshots = self.results.snapshots
        self.get_avg_std_of_curves(snapshots)
        self.get_x_plot()

        _, ax = plt.subplots(figsize = (8,6))
        ax.plot(self.x_plot, self.temp_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        ax.plot(self.x_plot, self.temp_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        ax.plot(self.x_plot, self.temp_sarea, marker = "o", markersize = 3, label = "Signed Area")
        ax.plot(self.x_plot, self.temp_samp, marker = "o", markersize = 3, label = "Signed Amp")     

        ax.fill_between(self.x_plot, self.temp_usarea-self.std_usarea, self.temp_usarea+self.std_usarea, color = 'blue', alpha = 0.2)
        ax.fill_between(self.x_plot, self.temp_usamp-self.std_usamp, self.temp_usamp+self.std_usamp, color = 'orange', alpha = 0.2)
        ax.fill_between(self.x_plot, self.temp_sarea-self.std_sarea, self.temp_sarea+self.std_sarea, color = 'green', alpha = 0.2)
        ax.fill_between(self.x_plot, self.temp_samp-self.std_samp, self.temp_samp+self.std_samp, color = 'red', alpha = 0.2)   

        ax.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        ax.tick_params(bottom=True,top=True,left=True,right=True)
        ax.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        ax.axhline(y = 0, color = "black")
        ax.set_legend(loc="upper right")
        ax.set_xlabel(r"$\mu=cos(\theta)$")
        ax.set_ylabel("(Area or Amp) (normalised) / $\mu$")
        ax.set_title(f"Num Snapshot(s): {len(snapshots)} Stokes V Signal (pos+neg) (normalised) {self.results.field_strength}G / $\mu$")
        return ax