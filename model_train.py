from read import getData as gd
from prototype.regression import RegModel as model

def main():
	g = gd()
	patientv = [pinfo[1:] for pname, pinfo in g.REMISSED_PATIENTS.items()]
	print len(patientv[0])
	m =  model(len(patientv[0])-2)
	train_in = [x[:265] for x in patientv[:120]]
	train_out = [x[266] for x in patientv[:120]]
	train_set= zip(train_out,train_in)
	m.train(train_set,0.01)
	test = [x[:266] for x in patientv[120:]]
	for x in test:
		x = np.insert(x,0,1)
		print m.reg(x)
if __name__ == "__main__":
	main()