import matplotlib.pyplot as plt
import numpy as np
from true_flux_analysers.profile_analyzer import ProfileAnalyzer
from true_flux_analysers.multiple_snapshot_wrapper import MultipleSnapshotWrapper

class TrueFluxPlotter:

    def __init__(self, ProfileWrapped: MultipleSnapshotWrapper) -> None:
        self.results = ProfileWrapped

    def get_x_plot(self):
        return self.results.mu_values
    
    
    def multiple_results_exist(self):
        return len(self.results.snapshots) > 1
    
    
    def snapshot_exists(self, snapshot):
       return snapshot in self.results.snapshots
    

    def get_snap_index(self, snapshot):
        self.snap_index = self.results.snapshots.index(snapshot)
    

    def get_temp_comb_curves(self):
        self.temp_samp = self.results.analyzer[self.snap_index].comb_normed_signed_amp
        self.temp_usamp = self.results.analyzer[self.snap_index].comb_normed_unsigned_amp
        self.temp_sarea = self.results.analyzer[self.snap_index].comb_normed_signed_area
        self.temp_usarea = self.results.analyzer[self.snap_index].comb_normed_unsigned_area


    def get_snapshot_comb_results(self, snapshot):
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_comb_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_comb_single_snapshot(self, snapshot):
        self.get_snapshot_comb_results(self,snapshot)

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
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (pos+neg) (normalised) {self.results[self.snap_index].field_strength}G / $\mu$")

    
    def get_temp_sep_curves(self):
        self.temp_pos_samp = self.results.analyzer[self.snap_index].pos_normed_signed_amp
        self.temp_pos_usamp = self.results.analyzer[self.snap_index].pos_normed_unsigned_amp
        self.temp_pos_sarea = self.results.analyzer[self.snap_index].pos_normed_signed_area
        self.temp_pos_usarea = self.results.analyzer[self.snap_index].pos_normed_unsigned_area

        self.temp_neg_samp = self.results.analyzer[self.snap_index].neg_normed_signed_amp
        self.temp_neg_usamp = self.results.analyzer[self.snap_index].neg_normed_unsigned_amp
        self.temp_neg_sarea = self.results.analyzer[self.snap_index].neg_normed_signed_area
        self.temp_neg_usarea = self.results.analyzer[self.snap_index].neg_normed_unsigned_area


    def get_snapshot_sep_results(self, snapshot):
        if self.snapshot_exists(snapshot):
            self.get_snap_index(snapshot)
            self.get_temp_sep_curves()
        else:
            print("Snapshot does not exist in", self.results.snapshots)


    def plot_pos_neg_single_snapshot(self, snapshot):
        self.get_snapshot_sep_results(self,snapshot)
        
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
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (pos) (normalised) {self.results[self.snap_index].field_strength}G / $\mu$")

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
        plt.title(f"(Snapshot: {snapshot} Stokes V Signal (neg) (normalised) {self.results[self.snap_index].field_strength}G / $\mu$")

        plt.show()


        """
        if self.multiple_results_exist():
            self.get_std_curves()
            plt.fill_between(self.x_plot, self.avg_usarea-self.std_usarea, self.avg_usarea+self.std_usarea, color = 'blue', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_usamp-self.std_usamp, self.avg_usamp+self.std_usamp, color = 'orange', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_sarea-self.std_sarea, self.avg_sarea+self.std_sarea, color = 'green', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_samp-self.std_samp, self.avg_samp+self.std_samp, color = 'red', alpha = 0.2)"""