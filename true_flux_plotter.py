import matplotlib.pyplot as plt
import numpy as np
from true_flux_analysers.profile_analyzer import ProfileAnalyzer

class TrueFluxPlotter:

    def __init__(self, profile_analyzer: ProfileAnalyzer) -> None:
        self.results = profile_analyzer

    def get_x_plot(self):
        return self.results.mu_values
    
    def get_avg_usarea(self):
        pass

    def multiple_results_exist(self):
        return len(self.results.num_snapshots) > 1

    def plot_pos_neg(self):
        plt.figure(figsize = (8,6))
        plt.plot(self.x_plot, self.avg_usarea, marker = "o", markersize = 3, label = "Unsigned Area")
        plt.plot(self.x_plot, self.avg_usamp, marker = "o", markersize = 3, label = "Unsigned Amp")
        plt.plot(self.x_plot, self.avg_sarea, marker = "o", markersize = 3, label = "Signed Area")
        plt.plot(self.x_plot, self.avg_samp, marker = "o", markersize = 3, label = "Signed Amp")

        if self.multiple_results_exist():
            plt.fill_between(self.x_plot, self.avg_usarea-self.std_usarea, self.avg_usarea+self.std_usarea, color = 'blue', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_usamp-self.std_usamp, self.avg_usamp+self.std_usamp, color = 'orange', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_sarea-self.std_sarea, self.avg_sarea+self.std_sarea, color = 'green', alpha = 0.2)
            plt.fill_between(self.x_plot, self.avg_samp-self.std_samp, self.avg_samp+self.std_samp, color = 'red', alpha = 0.2)

        plt.plot(np.linspace(0,1,10), np.linspace(1,1,10), color = 'black', linestyle = '--')
        plt.tick_params(bottom=True,top=True,left=True,right=True)
        plt.tick_params(labelbottom=True, labelleft= True, labelright = True, labeltop = True)
        plt.axhline(y = 0, color = "black")
        plt.legend(loc="upper right")
        plt.xlabel(r"$\mu=cos(\theta)$")
        plt.ylabel("(Area or Amp) (normalised) / $\mu$")
        plt.title("(Avgd 5) Stokes V Signal (pos+neg) (normalised) 200G / $\mu$")