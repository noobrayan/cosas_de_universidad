from appJar import *  # Imports all components of appJar

def ButtonHandler(select):  # Called when user clicks button
    if select == "Submit":  # If user clicks 'Submit'
        if program.getRadioButton("option") == "Yes":  # If user had chosen 'Yes'
            program.infoBox("Message", "Thank you for your positive feedback.")  # Displays message box
        else:  # If user had chosen 'No'
            program.infoBox("Message", "Nooooooooooooo!\n\n:(")  # Displays message box

    elif select == "More Info":  # If user clicks 'More Info'
        program.infoBox("More Info", "This is a demo of appJar.") # Displays message box

    elif select == "Close":  # If user clicks 'Close'
        quit()  # Close program


# Widgets
program = gui("Welcome!", "400x300")  # Sets size and title of main GUI
program.setBg("white")  # Sets background colour

# Image
# Remove the # at the start of the next two lines once you have specified a file path
# appJar prefers .gif files, so convert images to .gif before you use them
# A good converter can be found here: https://image.online-convert.com/convert-to-gif
program.addImage("logo", "logo1.gif") #careful, change the directory
program.zoomImage("logo", -10)  # Shrinks image

# Labels
program.addLabel("youtube", "Welcome To My Demo!")  # Title
program.setLabelBg("youtube", "light gray")  # Sets title background
program.addLabel("question", "Do you like my videos?")  # Label

# Radiobuttons
program.addRadioButton("option", "Yes")
program.addRadioButton("option", "No")

# Buttons
program.addButtons(["Submit", "More Info", "Close"], ButtonHandler)

program.go()  # Starts program