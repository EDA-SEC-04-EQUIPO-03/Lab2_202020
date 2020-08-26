import os
import sys
<<<<<<< HEAD
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
=======
file_path = os.path.join(os.path.dirname(__file__), '../..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))
data_dir = file_dir + '/Data/'
>>>>>>> origin/RamaGrupo3-j.lora
