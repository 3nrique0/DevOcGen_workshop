from snif import *
import os

gtime = 25 #generation time to scale the time in units of generation
target_scenario = "" #path to the .json file of the target scenario to add on the plots

for c in [6]:
#for c in [5, 6, 7]:
    for w in [0.5]:
    #for w in [0.5, 1]:
        h_inference_parameters = InferenceParameters(
	        data_source = './workshop_files/input_data/Pan_troglodytes_verus_Donald_inferred-model-004.ms', #path to the input file
	        source_type = SourceType.MSCommand, #type of input (SourceType.PSMC, SourceType.MS or SourceType.JSON)
	        IICR_type = IICRType.T_sim, #type of IICR (IICRType.Exact if the input is a PSMC or JSON file, IICRType.T_sim if the input is a ms command that simulates T2, IICRType.Seq_sim if the input is a ms command that simulates genetic sequences)
	        ms_reference_size = 352, #ms diploid deme size
	        ms_simulations = int(1e6), #number of coalescent times to simulate with ms
	        psmc_mutation_rate = 1.5e-8, #mutation rate used to scale the input psmc/iicr
	        psmc_number_of_sequences = None, #number of ms simulated sequences
	        psmc_length_of_sequences = None,	#length of ms simulated sequences
	        infer_scale = True, #whether to scale the results in generation time (True) or as T2 times (False)
	        data_cutoff_bounds = (1e4/gtime, 2e7/gtime), #time period of the input data, in units of generations if infer_scale = True
	        data_time_intervals = 64,  #time intervals of the psmc (parameter -p) / used to discretize the iicr
	        distance_function = ErrorFunction.ApproximatePDF, #function used for the distance computation (ApproximatePDF for the weighted method that depends on omega and is the preferred approach, or Visual)
	        distance_parameter = w, #omega parameter to modulate the fitting (if omega<1 it gives less weight to the recent past, if w>1 it gives more weight to the recent past)
	        distance_max_allowed = 7e3, #threshold of the distance computed between the source and inferred IICR
	        distance_computation_interval = (1e4/gtime, 2e7/gtime), #time period where the fitting will be computed, in units of generations if infer_scale = True
	        rounds_per_test_bounds = (30, 30), #interval of the number of rounds (or iterations) of the algorithm
	        repetitions_per_test = 2, #number of times to run SNIF (1 repetition corresponds to 1 inferred scenario)
	        number_of_components = c, #number of components	
	        bounds_islands = (2, 100), #range values for the number of demes
	        bounds_migrations_rates = (0.05, 50), #range values for the migration rates
# 	        bounds_migrations_rates = [(0.05, 50), (0.05, 50), (0.05, 50), (0.05, 50), (0.05, 50), (0.05, 50)],
	        bounds_deme_sizes = (1, 1), #range values for the size ratio (keep (1,1) for constant deme size)
# 	        bounds_deme_sizes = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)],
	        bounds_event_times = (1e4/gtime, 2e7/gtime), #time window(s) during which demographic events can occur, in units of generations if infer_scale = True
# 	        bounds_event_times = [(2e4/gtime, 1e5/gtime), (1e5/gtime, 3e5/gtime), (3e5/gtime, 6e5/gtime), (7e5/gtime, 1e6/gtime), (2e6/gtime, 5e6/gtime)],
	        bounds_effective_size = (10, 10000) #range values for the deme size, in numbers of diploids
	        )

        h_settings = Settings(
	        static_library_location = './libs/libsnif.so', #path to the library files, not to change
	        custom_filename_tag = 'Ptverus_Donald_fromT2', #custom tag added to the output name
	        output_directory = './workshop_files/SNIF_results', #path to the output directory
	        default_output_dirname = './SNIF_results_default' #default output directory, created if output_directory does not exist
	        )

         # Depending on wether you want to do the plotting with the inference altogether (options B and C) or not (option A), and wether you want to plot with the script snif2plot.py (option B) or the SNIF dedicated plotting function (option C), uncomment the corresponding block and comment the other two.
        
        # Option A. To launch the inference without doing any plot
        # infer(inf = h_inference_parameters, settings = h_settings)
        
        # Option B. Launching the inference and plotting using the script snif2plot.py
        basename = infer(inf = h_inference_parameters, settings = h_settings)
        if target_scenario == "":
            os.system(" ".join(["python3 ./snif2plot.py -bn", basename, "-g", str(gtime)]))
        else:
            os.system(" ".join(["python3 ./snif2plot.py -bn", basename, "-g", str(gtime), "-t", target_scenario]))
        
        # Option C. Launching the inference and plotting with SNIF plotting functions (requieres Latex and pgfplots >= 1.15)
        # basename = infer(inf = h_inference_parameters, settings = h_settings)
        # config = Configuration(
        # SNIF_basename = basename,
        # plot_width_cm = 13,
        # plot_height_cm = 6,
        # IICR_plots_style  = OutputStyle.Full,
        # PDF_plots_style = OutputStyle.Excluded,
        # CDF_plots_style = OutputStyle.Excluded,
        # islands_plot_style = OutputStyle.Excluded,
        # Nref_plot_style = OutputStyle.Excluded,
        # test_numbers = "all",
        # one_file_per_test = True,
        # versus_plot_style = OutputStyle.Excluded,
        # CG_style = OutputStyle.Excluded,
        # CG_size_history = False,
        # CG_source = '',
        # CG_source_legend = "",
        # Nref_histograms_bins = 100,
        # islands_histograms_bins = 100,
        # time_histograms_bins = 100,
        # migration_histograms_bins = 100,
        # size_histograms_bins = 100,
        # scaling_units = TimeScale.Years,
        # generation_time = 25
        # )
        # TeXify(config)
