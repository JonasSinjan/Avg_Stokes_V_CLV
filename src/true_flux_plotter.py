import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from .multiple_snapshot_wrapper import MultipleSnapshotWrapper

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
        self.get_snapshot_comb_results(snapshot)
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
        ax.legend(loc="upper right")
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


    def plot_pos_neg_single_snapshot(self, snapshot: int) -> np.array:
        self.get_snapshot_sep_results(snapshot)
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
        axarr[0].set_title(f"Snapshot: {snapshot} Stokes V Signal (pos) (normalised) {self.results.field_strength}G / $\mu$")

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
        axarr[1].set_title(f"Snapshot: {snapshot} Stokes V Signal (neg) (normalised) {self.results.field_strength}G / $\mu$")
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


    def plot_comb_multiple_snapshots(self, snapshots: list = None) -> mpl.axes:
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
        ax.legend(loc="upper right")
        ax.set_xlabel(r"$\mu=cos(\theta)$")
        ax.set_ylabel("(Area or Amp) (normalised) / $\mu$")
        ax.set_title(f"Num Snapshot(s): {len(snapshots)} Stokes V Signal (pos+neg) (normalised) {self.results.field_strength}G / $\mu$")
        return ax
    

    def avg_sep_curves(self) -> None:
        self.temp_pos_usarea = np.mean([self.results.analyzers[i].pos_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.temp_pos_usamp = np.mean([self.results.analyzers[i].pos_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.temp_pos_sarea = np.mean([self.results.analyzers[i].pos_normed_signed_area for i in self.snap_indices], axis = 0)
        self.temp_pos_samp = np.mean([self.results.analyzers[i].pos_normed_signed_amp for i in self.snap_indices], axis = 0)

        self.temp_neg_usarea = np.mean([self.results.analyzers[i].neg_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.temp_neg_usamp = np.mean([self.results.analyzers[i].neg_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.temp_neg_sarea = np.mean([self.results.analyzers[i].neg_normed_signed_area for i in self.snap_indices], axis = 0)
        self.temp_neg_samp = np.mean([self.results.analyzers[i].neg_normed_signed_amp for i in self.snap_indices], axis = 0)


    def std_sep_curves(self) -> None:
        self.std_pos_usarea = np.std([self.results.analyzers[i].pos_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.std_pos_usamp = np.std([self.results.analyzers[i].pos_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.std_pos_sarea = np.std([self.results.analyzers[i].pos_normed_signed_area for i in self.snap_indices], axis = 0)
        self.std_pos_samp = np.std([self.results.analyzers[i].pos_normed_signed_amp for i in self.snap_indices], axis = 0)

        self.std_neg_usarea = np.std([self.results.analyzers[i].neg_normed_unsigned_area for i in self.snap_indices], axis = 0)
        self.std_neg_usamp = np.std([self.results.analyzers[i].neg_normed_unsigned_amp for i in self.snap_indices], axis = 0)
        self.std_neg_sarea = np.std([self.results.analyzers[i].neg_normed_signed_area for i in self.snap_indices], axis = 0)
        self.std_neg_samp = np.std([self.results.analyzers[i].neg_normed_signed_amp for i in self.snap_indices], axis = 0)


    def get_avg_std_of_sep_curves(self, snapshots: list = None) -> None:
        if self.all_snapshots_exist(snapshots):
            self.get_snap_indices(snapshots)
            self.avg_sep_curves()
            self.std_sep_curves()
        else:
            print("Snapshots do not exist in", self.results.snapshots)

    
    def plot_pos_neg_multiple_snapshots(self, snapshots: list = None) -> np.array:
        if snapshots == None:
            snapshots = self.results.snapshots
        self.get_avg_std_of_sep_curves(snapshots)
        self.get_x_plot()

        _, axarr = plt.subplots(1,2,figsize = (16,6))
        axarr[0].plot(self.x_plot, self.temp_pos_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        axarr[0].plot(self.x_plot, self.temp_pos_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        axarr[0].plot(self.x_plot, self.temp_pos_sarea, marker = "o", markersize = 3, label = "Signed Area")
        axarr[0].plot(self.x_plot, self.temp_pos_samp, marker = "o", markersize = 3, label = "Signed Amp")        

        axarr[0].fill_between(self.x_plot, self.temp_pos_usarea-self.std_pos_usarea, self.temp_pos_usarea+self.std_pos_usarea, color = 'blue', alpha = 0.2)
        axarr[0].fill_between(self.x_plot, self.temp_pos_usamp-self.std_pos_usamp, self.temp_pos_usamp+self.std_pos_usamp, color = 'orange', alpha = 0.2)
        axarr[0].fill_between(self.x_plot, self.temp_pos_sarea-self.std_pos_sarea, self.temp_pos_sarea+self.std_pos_sarea, color = 'green', alpha = 0.2)
        axarr[0].fill_between(self.x_plot, self.temp_pos_samp-self.std_pos_samp, self.temp_pos_samp+self.std_pos_samp, color = 'red', alpha = 0.2)   

        axarr[0].plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        axarr[0].tick_params(bottom=True,top=True,left=True,right=True)
        axarr[0].tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        axarr[0].axhline(y = 0, color = "black")
        axarr[0].legend(loc="upper right")
        axarr[0].set_xlabel(r"$\mu=cos(\theta)$")
        axarr[0].set_ylabel("(Area or Amp) (normalised) / $\mu$")
        axarr[0].set_title(f"Num Snapshot(s): {len(snapshots)} Stokes V Signal (pos) (normalised) {self.results.field_strength}G / $\mu$")

        axarr[1].plot(self.x_plot, self.temp_neg_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        axarr[1].plot(self.x_plot, self.temp_neg_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        axarr[1].plot(self.x_plot, self.temp_neg_sarea, marker = "o", markersize = 3, label = "Signed Area")
        axarr[1].plot(self.x_plot, self.temp_neg_samp, marker = "o", markersize = 3, label = "Signed Amp")     

        axarr[1].fill_between(self.x_plot, self.temp_neg_usarea-self.std_neg_usarea, self.temp_neg_usarea+self.std_neg_usarea, color = 'blue', alpha = 0.2)
        axarr[1].fill_between(self.x_plot, self.temp_neg_usamp-self.std_neg_usamp, self.temp_neg_usamp+self.std_neg_usamp, color = 'orange', alpha = 0.2)
        axarr[1].fill_between(self.x_plot, self.temp_neg_sarea-self.std_neg_sarea, self.temp_neg_sarea+self.std_neg_sarea, color = 'green', alpha = 0.2)
        axarr[1].fill_between(self.x_plot, self.temp_neg_samp-self.std_neg_samp, self.temp_neg_samp+self.std_neg_samp, color = 'red', alpha = 0.2)      

        axarr[1].plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        axarr[1].tick_params(bottom=True,top=True,left=True,right=True)
        axarr[1].tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        axarr[1].axhline(y = 0, color = "black")
        axarr[1].legend(loc="upper right")
        axarr[1].set_xlabel(r"$\mu=cos(\theta)$")
        axarr[1].set_ylabel("(Area or Amp) (normalised) / $\mu$")
        axarr[1].set_title(f"Num Snapshot(s): {len(snapshots)} Stokes V Signal (neg) (normalised) {self.results.field_strength}G / $\mu$")
        return axarr
    

    def plot_stokes_v(self, snapshot: int, mu_indices: list, pos_or_neg: str = 'pos', xmax: int = 1750, xmin: int = -1750, ymin: float = -0.01, ymax: float = 0.01) -> None:
        """
        plot Stokes V signal for a given snapshot and mu values, and for a given viewing direction (pos or neg or both)

        Parameters
        ----------
        snapshot : int
            snapshot number
        mu_indices : list
            list of indices of the mu value(s) to plot - to see possible mu values: execute `self.get_x_plot()`, then `print(self.mu_values)`
        pos_or_neg : str
            'pos' for positive viewing direction, 'neg' for negative viewing direction, 'both' for both
        xmax : int
            maximum wavelength to plot
        xmin : int
            minimum wavelength to plot
        ymin : float
            minimum Stokes V value to plot
        ymax : float
            maximum Stokes V value to plot

        Returns
        -------
        None
        """
        self.get_snap_index(snapshot)
        analyzer = self.results.analyzers[self.snap_index]
        wavelengths = np.linspace(-1750,1750,251)
        if pos_or_neg == 'pos':
            mean_v =  analyzer.pos_signed_mean_v[12-i]
        elif pos_or_neg == 'neg':
            mean_v =  analyzer.neg_signed_mean_v[12-i]
        elif pos_or_neg == 'both':
            mean_v = (analyzer.pos_signed_mean_v[12-i] + analyzer.neg_signed_mean_v[12-i])/2
        plt.figure(figsize = (8,6))
        for i in mu_indices:
            plt.plot(wavelengths, mean_v/analyzer.Ic, label = f"$\mu = ${analyzer.mu_values[i]:.2g}", marker = "o", markersize = 2)
        plt.legend()
        plt.xlabel(r"Wavelength (m$\AA$)")
        plt.ylabel("Signed Mean Stokes V/Ic")
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.title(f"{analyzer.field_strength} G - snapshot: {analyzer.snapshot} - viewing direction: {pos_or_neg}")
        plt.show()


    def plot_avg_multiple_snapshots_stokes_v(self, snapshots: list, mu_indices: list, pos_or_neg: str = 'pos', xmax: int = 1750, xmin: int = -1750, ymin: float = -0.01, ymax: float = 0.01) -> None:
        """
        plot Stokes V signal for desired snapshot(s) and mu values, and for a given viewing direction (pos or neg or both)

        Parameters
        ----------
        snapshot : array_like
            snapshot number(s)
        mu_indices : list
            list of indices of the mu value(s) to plot - to see possible mu values: execute `self.get_x_plot()`, then `print(self.mu_values)`
        pos_or_neg : str
            'pos' for positive viewing direction, 'neg' for negative viewing direction, 'both' for both
        xmax : int
            maximum wavelength to plot
        xmin : int
            minimum wavelength to plot
        ymin : float
            minimum Stokes V value to plot
        ymax : float
            maximum Stokes V value to plot

        Returns
        -------
        None
        """
        stokes_v_stacked_over_mu = []
        for snapshot in snapshots:
            snap_index = self.results.snapshots.index(snapshot)
            if pos_or_neg == 'pos':
                stokes_v_stacked_over_mu.append(np.stack(self.results.analyzers[snap_index].pos_signed_mean_v/self.results.analyzers[snap_index].Ic))
            elif pos_or_neg == 'neg':
                stokes_v_stacked_over_mu.append(np.stack(self.results.analyzers[snap_index].neg_signed_mean_v/self.results.analyzers[snap_index].Ic))
            elif pos_or_neg == 'both':
                stokes_v_stacked_over_mu.append(np.stack((self.results.analyzers[snap_index].pos_signed_mean_v + self.results.analyzers[snap_index].neg_signed_mean_v)/(2*self.results.analyzers[snap_index].Ic)))
            
        v_over_mu_and_snap = np.stack(stokes_v_stacked_over_mu)
        v_avgd_over_snap = np.mean(v_over_mu_and_snap, axis = 0)
        v_std_over_snap = np.std(v_over_mu_and_snap, axis = 0)

        wavelengths = np.linspace(-1750,1750,251)
        plt.figure(figsize = (8,6))
        for i in mu_indices:
            plt.plot(wavelengths, v_avgd_over_snap[12-i,:], label = f"$\mu = ${self.results.analyzers[0].mu_values[i]:.2g}", marker = "o", markersize = 2)
            plt.fill_between(wavelengths,  v_avgd_over_snap[12-i,:]-v_std_over_snap[12-i,:], v_avgd_over_snap[12-i,:]+v_std_over_snap[12-i,:], alpha = 0.2)
        plt.legend()
        plt.xlabel(r"Wavelength (m$\AA$)")
        plt.ylabel("Signed Mean Stokes V/Ic")
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.title(f"{self.results.analyzers[0].field_strength} G - Num snapshots: {len(snapshots)} - viewing direction: {pos_or_neg}")
        plt.show()