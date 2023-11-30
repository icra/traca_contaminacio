from src.SWATPollution import SWATPollution
from src.pollution_utils import generate_pollution_observations, observacions_from_conca
from pathlib import Path
import sys
import pandas as pd
import json

if __name__ == '__main__':


    args = sys.argv[1:]
    contaminant = args[0]
    conca = args[1]

    if len (args) > 2:
        compound_features = json.loads(args[2])
    else:
        compound_features = {
            'pollutants.def': ('name', [
                (contaminant, 'solub', 5.89175657e+03),
                (contaminant, 'aq_hlife',  7.87844189e-01),
                (contaminant, 'aq_volat', 5.36559494e-05),
                (contaminant, 'aq_resus', 1.39548344e-02),
                (contaminant, 'aq_settle', 3.41342884e-02),
                (contaminant, 'ben_act_dep', 1.98351488e+00),
                (contaminant, 'ben_bury', 9.04084839e-03),
                (contaminant, 'ben_hlife', 4.34015290e-01),
                ])
        }
            
    cwd = Path(__file__).parent
    txt_in_out_path = cwd / 'data' / 'txtinouts' / f"TxtInOut_{conca}"

    channels_geom_path = cwd / 'data' / 'rivs1' / 'canals_tot_ci.shp'
    tmp_path = cwd / 'data' / 'txtinouts' / 'sims' / contaminant / conca 


    print(f"Començant simulació del contaminant {contaminant} a la conca {conca}:")

    observacions = generate_pollution_observations(contaminant)
    lod_path = cwd / 'data' / 'lod.xlsx'

    lod_path = cwd / 'data' / 'lod.xlsx'
    lod_df = pd.read_excel(lod_path, index_col=0)
    lod = lod_df.loc[contaminant, 'LOD (mg/L)']


    df = observacions_from_conca(channels_geom_path, observacions, conca)
    first_observation = df.year.min()
    year_end = 2022
    year_start = max(first_observation-3, 2000) #3 years warm-up
    warmup = max(1, first_observation - year_start)


    pollution_generator = SWATPollution(
        conca, 
        contaminant, 
        txt_in_out_path, 
        channels_geom_path,
        tmp_path,
        True,
        compound_features = compound_features,
        show_output = False,
        copy_txtinout = True,
        overwrite_txtinout = False,
        observacions=observacions,
        lod=lod, 
        year_start=year_start,
        year_end=year_end,
        warmup=warmup,
    )
    
    print(f"Finalitzada simulació del contaminant {contaminant} a la conca {conca}. Resultats guardats a :")
    print(pollution_generator.get_txtinout_path())