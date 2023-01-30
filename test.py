import csv
import json

neos_file =  './data/neos.csv'
cad_file = './data/cad.json'

#with open(neos_file, "r") as f:
#	reader = csv.DictReader(f)
#	NearEarthObject = []
    
#	for line in reader:
#		NearEarthObject.append(line)
	
#	print('NearEarthObject => ', NearEarthObject)

#cad = []
#with open(cad_file, 'r') as f:
#	json_data = json.load(f)

#	fields = json_data.get("fields")
#	close_approach_data = json_data.get('data')

#for close_approach in close_approach_data:
#	dict_data = {}

#	for index, field in enumerate(fields):
#		dict_data[field] = close_approach[index]

#	cad.append(dict_data)

#print(cad)

# [{'id': 'dK19Y030', 'spkid': '1003654', 'full_name': 'P/2019 Y3 (Catalina)', 'pdes': '2019 Y3', 'name': 'Catalina', 'prefix': 'P', 'neo': 'Y', 'pha': '', 'H': '', 'G': '', 'M1': '19.1', 'M2': '', 'K1': '4.5', 'K2': '', 'PC': '', 'diameter': '', 'extent': '', 'albedo': '', 'rot_per': '', 'GM': '', 'BV': '', 'UB': '', 'IR': '', 'spec_B': '', 'spec_T': '', 'H_sigma': '', 'diameter_sigma': '', 'orbit_id': 'JPL 3', 'epoch': '2458846.5', 'epoch_mjd': '58846', 'epoch_cal': '20191229.0000000', 'equinox': 'J2000', 'e': '.6957830663174389', 'a': '2.997858606129676', 'q': '.9119993527706466', 'i': '24.63522474375647', 'om': '139.3826941535015', 'w': '2.266734985153481', 'ma': '2.950878951276081', 'ad': '5.083717859488705', 'n': '.189883555717462', 'tp': '2458830.959533948970', 'tp_cal': '20191213.4595339', 'per': '1895.898771432654', 'per_y': '5.19068794368968', 'moid': '.0740474', 'moid_ld': '28.817026658', 'moid_jup': '.039495', 't_jup': '2.727', 'sigma_e': '7.4003E-5', 'sigma_a': '.0008002', 'sigma_q': '2.5158E-5', 'sigma_i': '.00072359', 'sigma_om': '.0029116', 'sigma_w': '.00098206', 'sigma_ma': '.0012713', 'sigma_ad': '.001357', 'sigma_n': '7.6027E-5', 'sigma_tp': '.00056696', 'sigma_per': '.75909', 'class': 'JFc', 'producer': 'Otto Matic', 'data_arc': '41', 'first_obs': '2019-12-17', 'last_obs': '2020-01-27', 'n_obs_used': '84', 'n_del_obs_used': '', 'n_dop_obs_used': '', 'condition_code': '6', 'rms': '.63285', 'two_body': '', 'A1': '', 'A2': '', 'A3': '', 'DT': ''}, {'id': 'dK19Y04d', 'spkid': '1003675', 'full_name': 'C/2019 Y4-D (ATLAS)', 'pdes': '2019 Y4-D', 'name': 'ATLAS', 'prefix': 'C', 'neo': 'Y', 'pha': '', 'H': '', 'G': '', 'M1': '13.3', 'M2': '15.5', 'K1': '4.5', 'K2': '5.', 'PC': '0.03', 'diameter': '', 'extent': '', 'albedo': '', 'rot_per': '', 'GM': '', 'BV': '', 'UB': '', 'IR': '', 'spec_B': '', 'spec_T': '', 'H_sigma': '', 'diameter_sigma': '', 'orbit_id': 'JPL 7', 'epoch': '2458953.5', 'epoch_mjd': '58953', 'epoch_cal': '20200414.0000000', 'equinox': 'J2000', 'e': '.9898679875903229', 'a': '25.09303807032235', 'q': '.2542429731250058', 'i': '44.95467243950517', 'om': '120.6559390884409', 'w': '177.7425034424157', 'ma': '359.630362575582', 'ad': '49.9318331675197', 'n': '.007841049682465823', 'tp': '2459000.641319005360', 'tp_cal': '20200531.1413190', 'per': '45912.22024839774', 'per_y': '125.700808346058', 'moid': '.626411', 'moid_ld': '243.78036887', 'moid_jup': '1.32993', 't_jup': '0.649', 'sigma_e': '.0046785', 'sigma_a': '11.388', 'sigma_q': '.0020356', 'sigma_i': '.49347', 'sigma_om': '.27222', 'sigma_w': '.23542', 'sigma_ma': '.25181', 'sigma_ad': '22.661', 'sigma_n': '.0053378', 'sigma_tp': '.023756', 'sigma_per': '31255.', 'class': 'HTC', 'producer': 'Davide Farnocchia', 'data_arc': '8', 'first_obs': '2020-04-09', 'last_obs': '2020-04-17', 'n_obs_used': '74', 'n_del_obs_used': '', 'n_dop_obs_used': '', 'condition_code': '9', 'rms': '.89276', 'two_body': '', 'A1': '', 'A2': '', 'A3': '', 'DT': ''}]

data = [{'id': 'dK19Y030', 'spkid': '1003654', 'full_name': 'P/2019 Y3 (Catalina)', 'pdes': '2019 Y3', 'name': 'Catalina', 'prefix': 'P', 'neo': 'Y', 'pha': '', 'H': '', 'G': '', 'M1': '19.1', 'M2': '', 'K1': '4.5', 'K2': '', 'PC': '', 'diameter': '', 'extent': '', 'albedo': '', 'rot_per': '', 'GM': '', 'BV': '', 'UB': '', 'IR': '', 'spec_B': '', 'spec_T': '', 'H_sigma': '', 'diameter_sigma': '', 'orbit_id': 'JPL 3', 'epoch': '2458846.5', 'epoch_mjd': '58846', 'epoch_cal': '20191229.0000000', 'equinox': 'J2000', 'e': '.6957830663174389', 'a': '2.997858606129676', 'q': '.9119993527706466', 'i': '24.63522474375647', 'om': '139.3826941535015', 'w': '2.266734985153481', 'ma': '2.950878951276081', 'ad': '5.083717859488705', 'n': '.189883555717462', 'tp': '2458830.959533948970', 'tp_cal': '20191213.4595339', 'per': '1895.898771432654', 'per_y': '5.19068794368968', 'moid': '.0740474', 'moid_ld': '28.817026658', 'moid_jup': '.039495', 't_jup': '2.727', 'sigma_e': '7.4003E-5', 'sigma_a': '.0008002', 'sigma_q': '2.5158E-5', 'sigma_i': '.00072359', 'sigma_om': '.0029116', 'sigma_w': '.00098206', 'sigma_ma': '.0012713', 'sigma_ad': '.001357', 'sigma_n': '7.6027E-5', 'sigma_tp': '.00056696', 'sigma_per': '.75909', 'class': 'JFc', 'producer': 'Otto Matic', 'data_arc': '41', 'first_obs': '2019-12-17', 'last_obs': '2020-01-27', 'n_obs_used': '84', 'n_del_obs_used': '', 'n_dop_obs_used': '', 'condition_code': '6', 'rms': '.63285', 'two_body': '', 'A1': '', 'A2': '', 'A3': '', 'DT': ''}, {'id': 'dK19Y04d', 'spkid': '1003675', 'full_name': 'C/2019 Y4-D (ATLAS)', 'pdes': '2019 Y4-D', 'name': 'ATLAS', 'prefix': 'C', 'neo': 'Y', 'pha': '', 'H': '', 'G': '', 'M1': '13.3', 'M2': '15.5', 'K1': '4.5', 'K2': '5.', 'PC': '0.03', 'diameter': '', 'extent': '', 'albedo': '', 'rot_per': '', 'GM': '', 'BV': '', 'UB': '', 'IR': '', 'spec_B': '', 'spec_T': '', 'H_sigma': '', 'diameter_sigma': '', 'orbit_id': 'JPL 7', 'epoch': '2458953.5', 'epoch_mjd': '58953', 'epoch_cal': '20200414.0000000', 'equinox': 'J2000', 'e': '.9898679875903229', 'a': '25.09303807032235', 'q': '.2542429731250058', 'i': '44.95467243950517', 'om': '120.6559390884409', 'w': '177.7425034424157', 'ma': '359.630362575582', 'ad': '49.9318331675197', 'n': '.007841049682465823', 'tp': '2459000.641319005360', 'tp_cal': '20200531.1413190', 'per': '45912.22024839774', 'per_y': '125.700808346058', 'moid': '.626411', 'moid_ld': '243.78036887', 'moid_jup': '1.32993', 't_jup': '0.649', 'sigma_e': '.0046785', 'sigma_a': '11.388', 'sigma_q': '.0020356', 'sigma_i': '.49347', 'sigma_om': '.27222', 'sigma_w': '.23542', 'sigma_ma': '.25181', 'sigma_ad': '22.661', 'sigma_n': '.0053378', 'sigma_tp': '.023756', 'sigma_per': '31255.', 'class': 'HTC', 'producer': 'Davide Farnocchia', 'data_arc': '8', 'first_obs': '2020-04-09', 'last_obs': '2020-04-17', 'n_obs_used': '74', 'n_del_obs_used': '', 'n_dop_obs_used': '', 'condition_code': '9', 'rms': '.89276', 'two_body': '', 'A1': '', 'A2': '', 'A3': '', 'DT': ''}]
name = 'catalina'

#neo_by_name = [item for item in data if item.get('name') == name]

#if not neo_by_name:
#	for neo in data:
#		neo_name = neo.get('name')
#		if neo_name and neo_name.strip().lower() == name:
#			neo_by_name.append(neo)

#def filter(d):
#	for approach in d:
#		yield approach

#generator = filter(data)

#print(next(generator))
#print(next(generator))
class NearEarthObject:
	def __init__(self, info):
		self.num = info

near = NearEarthObject(5)
print(near.num)

#data = {'des': '2020 AY1', 'orbit_id': '18', 'jd': '2458849.537524496', 'cd': '2020-Jan-01 00:54', 'dist': '0.0211660525256395', 'dist_min': '0.0211628345552616', 'dist_max': '0.0211692704882042', 'v_rel': '5.62203195551878', 'v_inf': '5.59959589405614', 't_sigma_f': '< 00:01', 'h': '25.1'}
#def test(**arg):
#	print(arg)