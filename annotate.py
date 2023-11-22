import cv2
import os
import keyboard
import time
import shutil

def main(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the file is an image
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Display the image
            img = cv2.imread(filepath)
            cv2.imshow('Image', img)
            cv2.waitKey(1)

            print(f"Reviewing: {filename}")

            # Wait for key press
            while True:
                time.sleep(0.01)
                if keyboard.is_pressed('right arrow'):


############################# To customize per annotating task ####################################

                    print("Textured:", filename)

                    # if lighting = 0
                    if filename[17] == '0':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Textured/0-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path = 'Outputs/Textured/0-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Textured/0-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                    # if lighting = 1
                    if filename[17] == '1':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Textured/1-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Textured/1-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Textured/1-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # if lighting = 2
                    if filename[17] == '2':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Textured/2-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Textured/2-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Textured/2-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # If lighting = 3
                    if filename[17] == '3':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Textured/3-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Textured/3-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Textured/3-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # If lighting = 4
                    if filename[17] == '4':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Textured/4-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Textured/4-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Textured/4-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    

                    break
                    ################################
                elif keyboard.is_pressed('left arrow'):

######################### To customize per annotating task ############################

                    print("Smooth:", filename)

                    # if lighting = 0
                    if filename[17] == '0':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Smooth/0-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Smooth/0-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Smooth/0-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                    # if lighting = 1
                    if filename[17] == '1':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Smooth/1-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Smooth/1-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Smooth/1-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # if lighting = 2
                    if filename[17] == '2':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Smooth/2-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Smooth/2-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Smooth/2-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # If lighting = 3
                    if filename[17] == '3':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Smooth/3-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Smooth/3-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Smooth/3-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)
                    
                    # If lighting = 4
                    if filename[17] == '4':
                        if filename[19] == 'B':
                            temp_file_path= 'Outputs/Smooth/4-Lighting/B'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'S':
                            temp_file_path= 'Outputs/Smooth/4-Lighting/S'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                        if filename[19] == 'T':
                            temp_file_path= 'Outputs/Smooth/4-Lighting/T'
                            if not os.path.exists(temp_file_path):
                                os.makedirs(temp_file_path)
                            shutil.copy(filepath, temp_file_path)

                    break

################################################################################
                elif keyboard.is_pressed('down arrow'):
                    print("Skip:", filename)
                    break

            cv2.destroyAllWindows()

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    main(directory)
