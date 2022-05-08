from tkinter import *
from tkinter import ttk
import tkinter.messagebox

n_p_s_lst = ["1/8",
         "1/4",
         "3/8",
         "1/2",
         "3/4",
         "1",
         "1 1/4",
         "1 1/2",
         "2",
         "2 1/2",
         "3",
         "3 1/2",
         "4",
         "5",
         "6",
         "8",
         "10",
         "12",
         "14",
         "16",
         "18",
         "20",
         "22",
         "24",
         "26",
         "28",
         "30",
         "32",
         "34",
         "36",
         "38",
         "40",
         "42",
         "44",
         "46",
         "48",
         "52",
         "56",
         "60",
         "64",
         "68",
         "72",
         "76",
         "80"]

pipe_grade_lst = ["B", "X42", "X46", "X52", "X56", "X60", "X65", "X70", "X80", "X90", "X100", "X120"]

design_factor_lst = [0.80, 0.72, 0.60, 0.50, 0.40]

o_d_inch_lst = [0.405,
            0.540,
            0.675,
            0.840,
            1.050,
            1.315,
            1.660,
            1.900,
            2.375,
            2.875,
            3.500,
            4.000,
            4.500,
            5.563,
            6.625,
            8.625,
            10.750,
            12.750,
            14.000,
            16.000,
            18.000,
            20.000,
            22.000,
            24.000,
            26.000,
            28.000,
            30.000,
            32.000,
            34.000,
            36.000,
            38.000,
            40.000,
            42.000,
            44.000,
            46.000,
            48.000,
            52.000,
            56.000,
            60.000,
            64.000,
            68.000,
            72.000,
            76.000,
            80.000]

pipe_smys_lst = [35500, 42100, 46400, 52200, 56600, 60200, 65300, 70300, 80500, 90600, 100100, 120400]

pipe_spec_no_lst = ["ASTM A53, Seamless", 
               "ASTM A53, Electric-resistance welded",
               "ASTM A53, Furnace-buttwelded, continuous weld",
               "ASTM A106, Seamless",
               "ASTM A134, Electric-fusion welded",
               "ASTM A135, Electric-resistance welded",
               "ASTM A139, Electric-fusion welded",
               "ASTM A333, Seamless",
               "ASTM A333, Electric-resistance welded",
               "ASTM A381, Submerged-arc welded",
               "ASTM A671, Electric-fusion welded, Classes 13, 23, 33, 43, 53",
               "ASTM A671, Electric-fusion welded, Classes 12, 22, 32, 42, 52",
               "ASTM A672, Electric-fusion welded, Classes 13, 23, 33, 43, 53",
               "ASTM A672, Electric-fusion welded, Classes 12, 22, 32, 42, 52",
               "ASTM A691, Electric-fusion welded, Classes 13, 23, 33, 43, 53",
               "ASTM A691, Electric-fusion welded, Classes 12, 22, 32, 42, 52",
               "API 5L, Electric-resistance welded",
               "API 5L, Seamless",
               "API 5L, Submerged-arc welded (straight seam or helical seam)",
               "API 5L, Furnace-buttwelded, Continuous weld",
               "API 5L, Combinition welded"]

long_weld_joint_factor_lst = [1.0, 1.0, 0.6, 1.0, 0.8, 1.0, 0.8, 1.0, 1.0, 1.0, 0.8, 1.0, 0.8, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 0.6, 1.0]

w_thk_inch_dic = {0.405:[0.095, 0.068, 0.057, 0.049],
            0.540:[0.119, 0.088, 0.073, 0.065],
            0.675:[0.126, 0.091, 0.073, 0.065],
            0.840:[0.294, 0.188, 0.147, 0.109, 0.095, 0.083, 0.065],
            1.050:[0.308, 0.219, 0.154, 0.113, 0.095, 0.083, 0.065],
            1.315:[0.358, 0.250, 0.179, 0.133, 0.114, 0.109, 0.065],
            1.660:[0.382, 0.250, 0.191, 0.140, 0.117, 0.109, 0.065],
            1.900:[0.400, 0.281, 0.2, 0.145, 0.125, 0.109, 0.065],
            2.375:[0.436, 0.344, 0.281, 0.250, 0.218, 0.188, 0.172, 0.154, 0.141, 0.125, 0.109, 0.083, 0.065],
            2.875:[0.552, 0.375, 0.276, 0.250, 0.216, 0.203, 0.188, 0.172, 0.156, 0.141, 0.125, 0.120, 0.109, 0.083],
            3.500:[0.600, 0.438, 0.300, 0.281, 0.250, 0.216, 0.188, 0.172, 0.156, 0.141, 0.125, 0.120, 0.109, 0.083],
            4.000:[0.318, 0.281, 0.250, 0.226, 0.188, 0.172, 0.156, 0.141, 0.125, 0.120, 0.109, 0.083],
            4.500:[0.674, 0.531, 0.438, 0.337, 0.312, 0.281, 0.250, 0.237, 0.219, 0.203, 0.188, 0.172, 0.156, 0.141, 0.125, 0.120, 0.109, 0.083],
            5.563:[0.750, 0.625, 0.500, 0.375, 0.344, 0.312, 0.281, 0.258, 0.219, 0.188, 0.156, 0.134, 0.125, 0.109, 0.083],
            6.625:[0.875, 0.864, 0.750, 0.719, 0.625, 0.562, 0.500, 0.432, 0.375, 0.344, 0.312, 0.280, 0.250, 0.219, 0.203, 0.188, 0.172, 0.156, 0.141, 0.134, 0.125, 0.109, 0.083],
            8.625:[1.000, 0.906, 0.875, 0.812, 0.750, 0.719, 0.625, 0.594, 0.562, 0.500, 0.438, 0.406, 0.375, 0.344, 0.322, 0.312, 0.277, 0.250, 0.219, 0.203, 0.188, 0.156, 0.148, 0.125, 0.109],
            10.750:[1.250, 1.125, 1.000, 0.938, 0.875, 0.844, 0.812, 0.719, 0.625, 0.594, 0.562, 0.500, 0.438, 0.365, 0.344, 0.307, 0.279, 0.250, 0.219, 0.203, 0.188, 0.165, 0.156, 0.134],
            12.750:[1.312, 1.250, 1.125, 1.062, 1.000, 0.938, 0.875, 0.844, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.438, 0.406, 0.375, 0.344, 0.330, 0.312, 0.281, 0.250, 0.219, 0.203, 0.188, 0.180, 0.172, 0.156],
            14.000:[2.500, 2.200, 2.125, 2.000, 1.406, 1.250, 1.125, 1.094, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.594, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.219, 0.210, 0.203, 0.188, 0.156],
            16.000:[1.594, 1.438, 1.250, 1.219, 1.188, 1.125, 1.062, 1.031, 1.000, 0.938, 0.875, 0.844, 0.812, 0.750, 0.688, 0.656, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.219, 0.203, 0.188, 0.165],
            18.000:[1.781, 1.562, 1.375, 1.250, 1.188, 1.156, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.219, 0.188, 0.165],
            20.000:[1.969, 1.750, 1.500, 1.375, 1.312, 1.281, 1.250, 1.188, 1.125, 1.062, 1.031, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.594, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.219, 0.188],
            22.000:[2.125, 1.875, 1.625, 1.500, 1.438, 1.375, 1.312, 1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.219, 0.188],
            24.000:[2.344, 2.062, 1.812, 1.562, 1.531, 1.500, 1.438, 1.375, 1.312, 1.250, 1.219, 1.188, 1.125, 1.062, 1.000, 0.969, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250, 0.218],
            26.000:[1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            28.000:[1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            30.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            32.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            34.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            36.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312, 0.281, 0.250],
            38.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312],
            40.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344, 0.312],
            42.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344],
            44.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344],
            46.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344],
            48.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375, 0.344],
            52.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375],
            56.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375],
            60.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375],
            64.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469, 0.438, 0.406, 0.375],
            68.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500, 0.469],
            72.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500],
            76.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562, 0.500],
            80.000:[1.250, 1.188, 1.125, 1.062, 1.000, 0.938, 0.875, 0.812, 0.750, 0.688, 0.625, 0.562]}


# ========== Solution section ==========
# Function to handle exceptions
def inputerror(error_message):
    tkinter.messagebox.showerror("ERROR", error_message)

# Function to do the main calculation
def calculate():
    try:
        design_pressure = float(entDesignPressure.get())
    except:
        error_message = " Incorrect design pressure!"
        inputerror(error_message)

    try:
        design_temperature = float(entDesignTemperature.get())
    except:
        error_message = " Incorrect design temperature!"
        inputerror(error_message)

    try:
        n_p_s = clickedNPS.get()
    except:
        error_message = " Incorrect NPS!"
        inputerror(error_message)

    pipe_grade = clickedPipeGrade.get()


    try:
        design_factor = float(clickedDesignFactor.get())
    except:
        error_message = " Incorrect design factor!"
        inputerror(error_message)

    try:
        pipe_spec = clickedPipeSpec.get()
    except:
        error_message = " Incorrect pipe spec. №!"
        inputerror(error_message)

    try:
        corrosion_allowance = float(entCorrosionAllowance.get())
    except:
        error_message = " Incorrect corrosion allowance!"
        inputerror(error_message)


    
    if design_temperature <= 121:
        temperature_derating_factor = 1
    elif 121 < design_temperature < 149:
        temperature_derating_factor = -0.0012 * design_temperature + 1.1457
    elif design_temperature == 149:
        temperature_derating_factor = 0.967
    elif 149 < design_temperature < 177:
        temperature_derating_factor = -0.0012 * design_temperature + 1.1457
    elif design_temperature == 177:
        temperature_derating_factor = 0.933
    elif 177 < design_temperature < 204:
        temperature_derating_factor = -0.0012 * design_temperature + 1.1457
    elif design_temperature == 204:
        temperature_derating_factor = 0.900
    elif 204 < design_temperature < 232:
        temperature_derating_factor = -0.0012 * design_temperature + 1.1457
    elif design_temperature == 232:
        temperature_derating_factor = 0.867

    n_p_s_index = n_p_s_lst.index(n_p_s)

    o_d_inch = o_d_inch_lst[n_p_s_index]

    try:
        pipe_grade_index = pipe_grade_lst.index(pipe_grade)
    except:
        error_message = " Incorrect pipe garde"
        inputerror(error_message)

    pipe_smys = pipe_smys_lst[pipe_grade_index]

    design_factor_index = design_factor_lst.index(design_factor)

    design_factor = design_factor_lst[design_factor_index]

    pipe_spec_no_index = pipe_spec_no_lst.index(pipe_spec)

    longitudinal_joint_factor = long_weld_joint_factor_lst[pipe_spec_no_index]

    

    calculated_wall_thickness = design_pressure * o_d_inch / (2 * pipe_smys * design_factor * temperature_derating_factor * longitudinal_joint_factor) + corrosion_allowance / 25.4

    lblCalculatedWallThickness_stringvar.set("{:.3f}".format(calculated_wall_thickness))

    w_thk_inch_lst = w_thk_inch_dic[o_d_inch]

    w_thk_inch_std = min(w_thk_inch_lst, key = lambda answer : abs(answer - calculated_wall_thickness))

    if w_thk_inch_std < calculated_wall_thickness:
        index_of_answer = w_thk_inch_lst.index(w_thk_inch_std)
        w_thk_inch_std = w_thk_inch_lst[index_of_answer - 1]
        lblSelecetdWallthicknessInchLabel_stringvar.set("Selected standard wall thickness: ")
        if w_thk_inch_std == w_thk_inch_lst[-1]:
            w_thk_inch_std = calculated_wall_thickness
            lblSelecetdWallthicknessInchLabel_stringvar.set("Selected non-standard wall thickness: ")

    w_thk_inch_std = "{:.3f}".format(w_thk_inch_std)

    lblSelectedWallthicknessInch_stringvar.set(w_thk_inch_std)
    



# ========== GUI section ==========

# START of the mail loop
main_window = Tk()
main_window.title("GPWT Calc")
#main_window.iconbitmap("c:/Users/AmirMousavian/OneDrive - northvolt.com/MY PYTHON PROJECTS/pipeline_calculation_notes/Aha-Soft-Transport-Pipe-line.ico")
#main_window.iconbitmap("Aha-Soft-Transport-Pipe-line.ico")

# ====>> Creating the required widgets
lblDesignPressure = Label(main_window, text="Design pressure: ")
entDesignPressure = Entry(main_window)
lblDesignPressureUnit = Label(main_window, text = " psig")

lblDesignTemperature = Label(main_window, text="Design temperature: ")
entDesignTemperature = Entry(main_window)
lblDesignTemperatureUnit = Label(main_window, text= " °C")

lblNPS = Label(main_window, text="NPS: ")
clickedNPS = StringVar()
clickedNPS.set("Select a value")
dropNPS = OptionMenu(main_window, clickedNPS, *n_p_s_lst)

lblPipeGrade = Label(main_window, text="Pipe grade: ")
clickedPipeGrade = StringVar()
clickedPipeGrade.set("Select a value")
dropPipeGrade = OptionMenu(main_window, clickedPipeGrade, *pipe_grade_lst)
lblPipeGradeUnit = Label(main_window, text=" psi")

lblDesignFactor = Label(main_window, text="Design factor: ")
clickedDesignFactor = StringVar()
clickedDesignFactor.set("Select a value")
dropDesignFactor = OptionMenu(main_window, clickedDesignFactor, *design_factor_lst)

lblPipeSpec = Label(main_window, text="Pipe spec. №: ")
clickedPipeSpec = StringVar()
clickedPipeSpec.set("Select a value")
dropPipeSpec = OptionMenu(main_window, clickedPipeSpec, *pipe_spec_no_lst)

lblCorrosionAllowance = Label(main_window, text="Corrosion allowance: ")
entCorrosionAllowance = Entry(main_window)
lblCorrosionAllowanceUnit = Label(main_window, text=" mm")

btnCalculate = Button(main_window, text="CALCULATE", width=30, bg="orange", fg="white", command=calculate)

separator_01 = ttk.Separator(main_window, orient="horizontal")

lblCalculatedWallThickness_stringvar = StringVar()
lblCalculatedWallThickness_stringvar.set("")
lblCalculatedWallThickness = Label(main_window, text="Calculated wall thickness: ")
lblCalculatedWallThicknessValue = Label(main_window, textvariable=lblCalculatedWallThickness_stringvar)
lblCalculatedWallThicknessUnit = Label(main_window, text="inch")

lblSelectedWallthicknessInch_stringvar = StringVar()
lblSelectedWallthicknessInch_stringvar.set("")
lblSelecetdWallthicknessInchLabel_stringvar = StringVar()
lblSelecetdWallthicknessInchLabel_stringvar.set("Selected standard wall thickness: ")
lblSelectedWallthicknessInch = Label(main_window, textvariable=lblSelecetdWallthicknessInchLabel_stringvar, font="Helvetica 10 bold")
lblSelectedWallthicknessInchValue = Label(main_window, textvariable=lblSelectedWallthicknessInch_stringvar, font="Helvetica 10 bold")
lblSelectedWallthicknessInchUnit = Label(main_window, text="inch", font="Helvetica 10 bold")

separator_02 = ttk.Separator(main_window, orient="horizontal")

lblDisclaimer = Label(main_window, text="This application is made as per the requirments of ASME B31.8 - 2014,"
                      "\nAPI Spec. 5L -45th edition and ASME B36.10M - 2004."
                      "\nThe application is still under development. In case of any breakdown \nor error please contact the developer via amirmsn@gmail.com.", justify=LEFT, font="Helvetica 8")

# <<==== Shoving the widgets into the window
lblDesignPressure.grid(row=0, column=0, sticky="w")
entDesignPressure.grid(row=0, column=1, ipady=5, pady=10)
lblDesignPressureUnit.grid(row=0, column=2, sticky="w")

lblDesignTemperature.grid(row=1, column=0, sticky="w")
entDesignTemperature.grid(row=1, column=1, ipady=5, pady=10)
lblDesignTemperatureUnit.grid(row=1, column=2, sticky="w")

lblNPS.grid(row=2, column=0, sticky="w")
dropNPS.grid(row=2, column=1, ipady=5, pady=5)

lblPipeGrade.grid(row=3, column=0, sticky="w")
dropPipeGrade.grid(row=3, column=1, ipady=5, pady=5)
lblPipeGradeUnit.grid(row=3, column=2, sticky="w")

lblDesignFactor.grid(row=4, column=0, sticky="w")
dropDesignFactor.grid(row=4, column=1, ipady=5, pady=5)

lblPipeSpec.grid(row=5, column=0, sticky="w")
dropPipeSpec.grid(row=5, column=1, ipady=5, pady=5)

lblCorrosionAllowance.grid(row=6, column=0, sticky="w")
entCorrosionAllowance.grid(row=6, column=1, ipady=5, pady=10)
lblCorrosionAllowanceUnit.grid(row=6, column=2, sticky="w")

btnCalculate.grid(row=7, column=0, columnspan=3)

separator_01.grid(row=8, columnspan=3, pady=10, sticky="ew")

lblCalculatedWallThickness.grid(row=9, column=0, sticky="w")
lblCalculatedWallThicknessValue.grid(row=9, column=1, pady=5)
lblCalculatedWallThicknessUnit.grid(row=9, column=2, sticky="w")

lblSelectedWallthicknessInch.grid(row=10, column=0, sticky="w")
lblSelectedWallthicknessInchValue.grid(row=10, column=1, pady=5)
lblSelectedWallthicknessInchUnit.grid(row=10, column=2, sticky="w")

separator_02.grid(row=11, columnspan=3, pady=10, sticky="ew")

lblDisclaimer.grid(row=12, columnspan=3, sticky="w")


# Preventing the size of the main window to be changed by the user
main_window.resizable(False, False)

#main_window.geometry("310x325")

# END of the main loop
main_window.mainloop()

# ===================== FINAL NOTE =====================
# Converting the .py file to .exe file considering pyinstaller is installed
# Being in the .py directory
# pyinstaller --onefile --noconsole gas_pipeline_wall_thickness_calculator_rev_01.py
# pyinstaller.exe --icon=Aha-Soft-Transport-Pipe-line.ico -F --noconsole gas_pipeline_wall_thickness_calculator_rev_01.py