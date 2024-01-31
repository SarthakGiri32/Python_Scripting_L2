# code for testing mkdir method
import os
print('The Test directory name is "TestDirectory"')
os.mkdir("TestDirectory")
print('Changing the current working directory to "TestDirectory"')
os.chdir("TestDirectory")
print(f'Displaying the current working directory: "{os.getcwd()}"')
original_working_directory = \
    r"C:\\Users\\giris\\Documents\\MySkillz\\Training\\Python_Scripting_L2\\Python_Scripting\\File_Operations"
print(f'')
