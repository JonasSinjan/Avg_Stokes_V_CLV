import numpy as np
from astropy.io import fits
import scipy.integrate as spi

class ProfileAnalyzer():
    
    def __init__(self, dir, field_strength, snapshot, negang_str = '-') -> None:
        self.dir = dir
        self.field_strength = field_strength
        self.snapshot = snapshot
        self.negang_str = negang_str
        self.mu_values = [0.0486,0.1007,0.1493,0.2014,0.25,0.2986,0.3993,0.5,0.6007,0.7014,0.7986,0.8993,1.0]
        self.angles = ['00','25_9','37','45_5','53','60','66_5','72_6','75_5','78_4','81_4','84_2','87_2']


    def get_profiles(self):
        ang = ['00','25_9','37','45_5','53','60','66_5','72_6','75_5','78_4','81_4','84_2','87_2']
        self.pos_profiles = []
        self.neg_profiles = []

        for i in range(13):
            profile_path = f'/export/local/scratch/sinjan/spinor_fwd/{self.dir}/{self.snapshot}/6173_masi_theta{ang[i]}/inverted_profs.1.fits'
            self.pos_profiles.append(fits.getdata(profile_path))
            if ang[i] == '00':
                neg_str = ''
            else:
                neg_str = self.negang_str
            neg_profile_path = profile_path.split('theta')[0] + "theta" + str(neg_str) + profile_path.split('theta')[1]
            self.neg_profiles.append(fits.getdata(neg_profile_path))
    

    def get_Ic(self):
        self.Ic = self.pos_profiles[0][:,:,0,:50].mean()


    def get_stokes_I(self):
        self.pos_I = [x[:,:,0,:].mean(axis=(0,1)) for x in self.pos_profiles]
        self.neg_I = [x[:,:,0,:].mean(axis=(0,1)) for x in self.neg_profiles]


    def get_stokes_V(self):
        self.pos_v = [x[:,:,1,:] for x in self.pos_profiles]
        self.neg_v = [x[:,:,1,:] for x in self.neg_profiles]


    def get_mean_stokes_V(self):
        self.pos_signed_mean_v =  [x.mean(axis = (0,1)) for x in self.pos_v]
        self.neg_signed_mean_v =  [x.mean(axis = (0,1)) for x in self.neg_v]
        

    def get_abs_mean_stokes_V(self):
        self.pos_unsigned_mean_v =  [np.abs(x).mean(axis = (0,1)) for x in self.pos_v]
        self.neg_unsigned_mean_v =  [np.abs(x).mean(axis = (0,1)) for x in self.neg_v]


    def get_mean_abs_stokes_V(self):
        self.pos_mean_unsigned_mean_v =  [np.abs(x.mean(axis = (0,1))) for x in self.pos_v]
        self.neg_mean_unsigned_mean_v =  [np.abs(x.mean(axis = (0,1))) for x in self.neg_v]

                
    def del_profiles(self):
        del self.pos_profiles
        del self.neg_profiles
        del self.pos_v
        del self.neg_v


    def check_if_5250(self):
        if '5250' in self.dir:
            return True


    def get_avg_amp(self, avg_v):
        if self.check_if_5250():
            start = 100
            end = 141
        else:
            start = 100
            end = 151
        return [np.mean([abs(np.max(x[start:end]/self.Ic)), abs(np.min(x[start:end]/self.Ic))]) for x in avg_v]


    def get_abs_area(self, avg_v):
        if self.check_if_5250():
            start = 100
            end = 141
        else:
            start = 100
            end = 151
        WAVELENGTH_STEP_SIZE = 0.014 #Angstrom
        return [spi.simpson(abs(x[start:end]/self.Ic), dx = WAVELENGTH_STEP_SIZE) for x in avg_v]#np.trapz
    
    def get_fringe_abs_area(self, avg_v):
        WAVELENGTH_STEP_SIZE = 0.014 #Angstrom
        return [spi.simpson(abs(x[100:111]/self.Ic), dx = WAVELENGTH_STEP_SIZE) + spi.simpson(abs(x[135:151]/self.Ic), dx = WAVELENGTH_STEP_SIZE) for x in avg_v]#np.trapz
    

    def get_area(self, avg_v):
        if self.check_if_5250():
            start = 100
            end = 141
        else:
            start = 100
            end = 151
        WAVELENGTH_STEP_SIZE = 0.014 #Angstrom
        return [spi.simpson(x[start:end]/self.Ic, dx = WAVELENGTH_STEP_SIZE) for x in avg_v]


    def get_mean_signed_and_unsigned_stokes_vs(self):
        self.get_profiles()
        self.get_stokes_I()
        self.get_Ic()
        self.get_stokes_V()
        self.get_mean_stokes_V()
        #self.get_mean_abs_stokes_V()
        self.get_abs_mean_stokes_V()
        self.del_profiles()
        
        
    def get_5250_fringe_line_frac(self):
        self.get_mean_signed_and_unsigned_stokes_vs()
        self.pos_unsigned_area = self.get_abs_area(self.pos_signed_mean_v)
        self.neg_unsigned_area = self.get_abs_area(self.neg_signed_mean_v)
        
        self.pos_funsigned_area = self.get_fringe_abs_area(self.pos_signed_mean_v)
        self.neg_funsigned_area = self.get_fringe_abs_area(self.neg_signed_mean_v)

        self.pos_frac = [np.round(i/j,3) for i,j in zip(self.pos_funsigned_area, self.pos_unsigned_area)]
        self.neg_frac = [np.round(i/j,3) for i,j in zip(self.neg_funsigned_area, self.neg_unsigned_area)]
        

    def get_pos_stokes_v_proxy_strengths(self):
        self.pos_signed_amp = self.get_avg_amp(self.pos_signed_mean_v)
        self.pos_abs_mean_amp = self.get_avg_amp(self.pos_unsigned_mean_v) #not useful
        self.pos_signed_area = self.get_area(self.pos_signed_mean_v)
        self.pos_unsigned_area = self.get_abs_area(self.pos_signed_mean_v) #changed to get_abs_area


    def return_pos_stokes_v_proxy_strengths_as_list(self):
        return [self.pos_signed_amp, self.pos_abs_mean_amp, self.pos_signed_area, self.pos_unsigned_area]
    

    def get_neg_stokes_v_proxy_strengths(self):
        self.neg_signed_amp = self.get_avg_amp(self.neg_signed_mean_v)
        self.neg_abs_mean_amp = self.get_avg_amp(self.neg_unsigned_mean_v) #not useful
        self.neg_signed_area = self.get_area(self.neg_signed_mean_v)
        self.neg_unsigned_area = self.get_abs_area(self.neg_signed_mean_v)


    def return_neg_stokes_v_proxy_strengths_as_list(self):
        return [self.neg_signed_amp, self.neg_abs_mean_amp, self.neg_signed_area, self.neg_unsigned_area]


    def norm_curves_by_mu_and_mu_is_1_value(self):
        self.pos_normed_signed_amp = np.flip(self.pos_signed_amp)/self.pos_signed_amp[0]/self.mu_values
        self.pos_normed_abs_mean_amp = np.flip(self.pos_abs_mean_amp)/self.pos_abs_mean_amp[0]/self.mu_values
        self.pos_normed_signed_area = np.flip(self.pos_signed_area)/self.pos_signed_area[0]/self.mu_values
        self.pos_normed_unsigned_area = np.flip(self.pos_unsigned_area)/self.pos_unsigned_area[0]/self.mu_values

        self.neg_normed_signed_amp = np.flip(self.neg_signed_amp)/self.pos_signed_amp[0]/self.mu_values
        self.neg_normed_abs_mean_amp = np.flip(self.neg_abs_mean_amp)/self.pos_abs_mean_amp[0]/self.mu_values
        self.neg_normed_signed_area = np.flip(self.neg_signed_area)/self.pos_signed_area[0]/self.mu_values
        self.neg_normed_unsigned_area = np.flip(self.neg_unsigned_area)/self.pos_unsigned_area[0]/self.mu_values


    def norm_curves_by_mu(self):
        self.pos_normed_signed_amp = np.flip(self.pos_signed_amp)/self.mu_values
        self.pos_normed_abs_mean_amp = np.flip(self.pos_abs_mean_amp)/self.mu_values
        self.pos_normed_signed_area = np.flip(self.pos_signed_area)/self.mu_values
        self.pos_normed_unsigned_area = np.flip(self.pos_unsigned_area)/self.mu_values

        self.neg_normed_signed_amp = np.flip(self.neg_signed_amp)/self.mu_values
        self.neg_normed_abs_mean_amp = np.flip(self.neg_abs_mean_amp)/self.mu_values
        self.neg_normed_signed_area = np.flip(self.neg_signed_area)/self.mu_values
        self.neg_normed_unsigned_area = np.flip(self.neg_unsigned_area)/self.mu_values


    def return_pos_neg_normed_curves_as_lists(self):
        return [self.pos_normed_signed_amp, self.pos_normed_abs_mean_amp, self.pos_normed_signed_area, self.pos_normed_unsigned_area], [self.neg_normed_signed_amp, self.neg_normed_abs_mean_amp, self.neg_normed_signed_area, self.neg_normed_unsigned_area]
    

    def combine_pos_neg_normed_curves(self):
        self.comb_normed_curves = [np.add(x,y)/2 for x,y in zip(self.return_pos_neg_normed_curves_as_lists()[0], self.return_pos_neg_normed_curves_as_lists()[1])]
        self.comb_normed_signed_amp = self.comb_normed_curves[0]
        self.comb_normed_abs_mean_amp = self.comb_normed_curves[1]
        self.comb_normed_signed_area = self.comb_normed_curves[2]
        self.comb_normed_unsigned_area = self.comb_normed_curves[3]
    

    def run_analysis(self):
        self.get_mean_signed_and_unsigned_stokes_vs()
        self.get_pos_stokes_v_proxy_strengths()
        self.get_neg_stokes_v_proxy_strengths()
        self.norm_curves_by_mu_and_mu_is_1_value() #point of optionality with norm_curves_by_mu() - ie do mu=1 normalization at a later point
        self.combine_pos_neg_normed_curves()