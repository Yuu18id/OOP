class Bayu:
	
	pengunjung = 0
	
	def __init__(self):
		self.dataMhs = {'nim' : ['1', '2', '3'], 'nama':['Bayu', 'Bagas', 'Budi'], 'jurusan' : ['TI', 'IF', 'AK'], 'semester' : ['3', '3', '5']}
		self.dataDosen = {'nip' : ['1', '2', '3'], 'nama':['Arya', 'Beti', 'Rizal'], 'jabatan' : ['Dosen Tetap', 'Dosen Honorer', 'Dekan'], 'jkelamin' : ['Laki-Laki', 'Perempuan', 'Laki-Laki'], 'noHp': ['0899', '0812', '0853']}
		self.pengunjung = 0
		
	def cetakMhs(self):
		for i in range(len(self.dataMhs['nim'])):
			print('NIM : ',self.dataMhs['nim'][i])
			print('Nama : ', self.dataMhs['nama'][i])
			print('Jurusan : ', self.dataMhs['jurusan'][i])
			print('Semester : ', self.dataMhs['semester'][i])
			print('\n')
		pengunjung += i
		
	def cetakDosen(self):
		for i in range(len(self.dataDosen['nip'])):
			print('NIP : ',self.dataDosen['nip'][i])
			print('Nama : ', self.dataDosen['nama'][i])
			print('Jabatan : ', self.dataDosen['jabatan'][i])
			print('Jenis Kelamin : ', self.dataDosen['jkelamin'][i])
			print('No. HP : ', self.dataDosen['noHp'][i])
			print('\n')
		pengunjung += i
		
class Absensi(Bayu):
	
	def banyak(self):
		print(pengunjung)
		
Bayu().cetakMhs()
Bayu().cetakDosen()
Absensi().banyak()