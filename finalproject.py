import matplotlib.pyplot as plt


def school_salaries(filename):
    """
    takes a file with university names and salaries, and finds the average salary of each university

    :param filename: (file) a file with university names and salaries
    :return: (dict) a dictionary of each school, and it's associated average salaries
    """
    avg_salary = {}
    new_list = []
    avg_salary_counter = {}
    with open(filename, "r") as file_in:
        count = 0
        for row in file_in:

            # makes ure the header is skipped
            if count >= 1:
                for item in row.split(","):

                    # creates a new list of the split row
                    if len(new_list) <= 6:
                        new_list.append(item.replace('"', ""))
                    if len(new_list) >= 6:

                        # iterates through the split row, and breaks of there is a ValueError. I did this to cut the
                        # file down shorter as me and my partner were asked, and to avoid errors
                        try:

                            # adds the salary value to the dict if the school exists in the dictionary, adds the key and
                            # starts the new value for that key if not
                            if str(new_list[1]) in avg_salary.keys():
                                avg_salary[str(new_list[1])] += float(new_list[4])
                                avg_salary_counter[str(new_list[1])] += 1
                                print(avg_salary)
                            else:
                                avg_salary[str(new_list[1])] = float(new_list[4])
                                avg_salary_counter[str(new_list[1])] = 1
                        except ValueError:
                            break
            new_list = []
            count += 1

        # iterates through the keys and finds the average for each school
        for school in avg_salary.keys():
            avg_salary[school] = avg_salary[school] / avg_salary_counter[school]
        return avg_salary


def avg_salary_bar_graph_schools(avg_salary):
    """
    takes average salary data from each school and creates a bar graph comparing them

    :param avg_salary: (dict) a dictionary in the style created by average_salary
    :return: a bar graph
    """
    school_list = ["Akron", "Ohio State", "Miami", "Green State", "Central State", "Ohio", "Youngstown", "Cincinnati",
                   "Kent State", "Wright State", "Toledo", "Cleveland", "Shawnee State"]
    avg_salaries = avg_salary.values()

    plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.rcParams['font.size'] = 7
    plt.bar(school_list, avg_salaries, color='maroon',
            width=0.4)
    plt.xlabel("Universities")
    plt.ylabel("Average Salaries")
    plt.title("Average Salaries Compared Across Universities")
    plt.show()


def dept_salaries(filename):
    """
    takes a file with department names and salaries, and finds the average salary of each department

    :param filename: (file) a file with departments and salaries
    :return: (dict) a dict of each department associated with the average salary from that department
    """
    new_list = []
    avg_salary = {}
    avg_salary_counter = {}
    with open(filename, "r") as file_in:
        count = 0
        for row in file_in:

            # makes ure the header is skipped
            if count >= 1:
                for item in row.split(","):
                    if len(new_list) <= 6:
                        new_list.append(item.replace('"', ""))
                    if len(new_list) >= 6:

                        # iterates through the split row, and breaks of there is a ValueError. I did this to cut the
                        # file down shorter as me and my partner were asked, and to avoid errors
                        try:

                            # adds the salary value to the dict if the department exists in the dictionary, adds the
                            # key and starts the new value for that key if not
                            if "Athletics" in avg_salary.keys() and "Athletics" in str(new_list[3]):
                                avg_salary["Athletics"] += float(new_list[4])
                                avg_salary_counter["Athletics"] += 1
                            if "Athletics" not in avg_salary.keys():
                                avg_salary["Athletics"] = float(new_list[4])
                                avg_salary_counter["Athletics"] = 1
                            if "Sociology" in avg_salary.keys() and "Sociology" in str(new_list[3]):
                                avg_salary["Sociology"] += float(new_list[4])
                                avg_salary_counter["Sociology"] += 1
                            if "Sociology" not in avg_salary.keys():
                                avg_salary["Sociology"] = float(new_list[4])
                                avg_salary_counter["Sociology"] = 1
                            if "Art" in avg_salary.keys() and "Art" in str(new_list[3]):
                                avg_salary["Art"] += float(new_list[4])
                                avg_salary_counter["Art"] += 1
                            if "Art" not in avg_salary.keys():
                                avg_salary["Art"] = float(new_list[4])
                                avg_salary_counter["Art"] = 1
                            if "Economics" in avg_salary.keys() and "Economics" in str(new_list[3]):
                                avg_salary["Economics"] += float(new_list[4])
                                avg_salary_counter["Economics"] += 1
                            if "Economics" not in avg_salary.keys():
                                avg_salary["Economics"] = float(new_list[4])
                                avg_salary_counter["Economics"] = 1
                            if "Neuroscience" in avg_salary.keys() and "Neuroscience" in str(new_list[3]):
                                avg_salary["Neuroscience"] += float(new_list[4])
                                avg_salary_counter["Neuroscience"] += 1
                            if "Neuroscience" not in avg_salary.keys():
                                avg_salary["Neuroscience"] = float(new_list[4])
                                avg_salary_counter["Neuroscience"] = 1
                            if "History" in avg_salary.keys() and "History" in str(new_list[3]):
                                avg_salary["History"] += float(new_list[4])
                                avg_salary_counter["History"] += 1
                            if "History" not in avg_salary.keys():
                                avg_salary["History"] = float(new_list[4])
                                avg_salary_counter["History"] = 1
                            if "Computer Science" in avg_salary.keys() and "Computer Science" in str(new_list[3]):
                                avg_salary["Computer Science"] += float(new_list[4])
                                avg_salary_counter["Computer Science"] += 1
                            if "Computer Science" not in avg_salary.keys():
                                avg_salary["Computer Science"] = float(new_list[4])
                                avg_salary_counter["Computer Science"] = 1
                        except ValueError:
                            break
            new_list = []
            count += 1

        # iterates through the keys and finds the average for each department
        for department in avg_salary.keys():
            avg_salary[department] = avg_salary[department] / avg_salary_counter[department]
        return avg_salary


def avg_salary_bar_graph_dept(avg_salary):
    """
    takes average salary data from each department and creates a bar graph comparing them

    :param avg_salary: (dict) a dictionary in the style created by dept_salaries
    :return: a bar graph
    """
    departments = avg_salary.keys()
    avg_salaries = avg_salary.values()

    plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.rcParams['font.size'] = 7
    plt.bar(departments, avg_salaries, color='maroon',
            width=0.4)
    plt.xlabel("Departments")
    plt.ylabel("Average Salaries")
    plt.title("Average Salaries Compared Across Departments")
    plt.show()


def tenure_salary_change(filename, boolean):
    """
    takes a file and bool as input, and searches for the average salaries from the years included in the file for
    tenured professors if bool is true, and non-tenured if bool is false

    :param filename: (file) file in the same style as before, with dates and tenured/non-tenured data
    :param boolean: (bool) a boolean
    :return: (dict) a dictionary of years and their associated average tenured/non-tenured salaries
    """
    sorted_tenured_dict = {}
    sorted_non_tenured_dict = {}
    avg_salary_tenured = {}
    avg_salary_non_tenured = {}
    new_list = []
    avg_salary_counter_tenured = {}
    avg_salary_counter_non_tenured = {}
    with open(filename, "r") as file_in:
        count = 0
        for row in file_in:

            # makes ure the header is skipped
            if count >= 1:
                for item in row.split(","):
                    if len(new_list) <= 6:
                        new_list.append(item.replace('"', ""))
                    if len(new_list) >= 6:

                        # iterates through the split row, and breaks of there is a ValueError. I did this to cut the
                        # file down shorter as me and my partner were asked, and to avoid errors
                        try:

                            # if bool is true, searches for tenured staff and adds their salaries to the dictionary
                            if boolean:
                                if "Tenure" in new_list[2] and "Non" not in new_list[2]:
                                    if new_list[5][0:4] in avg_salary_tenured.keys():
                                        avg_salary_tenured[new_list[5][0:4]] += float(new_list[4])
                                        avg_salary_counter_tenured[new_list[5][0:4]] += 1
                                    if new_list[5][0:4] not in avg_salary_tenured.keys():
                                        avg_salary_tenured[new_list[5][0:4]] = float(new_list[4])
                                        avg_salary_counter_tenured[new_list[5][0:4]] = 1

                            # if bool is false, searches for non-tenured staff and adds their salaries to the dictionary
                            else:
                                if "Tenure" not in new_list[2]:
                                    if new_list[5][0:4] in avg_salary_non_tenured.keys():
                                        avg_salary_non_tenured[new_list[5][0:4]] += float(new_list[4])
                                        avg_salary_counter_non_tenured[new_list[5][0:4]] += 1
                                    if new_list[5][0:4] not in avg_salary_non_tenured.keys():
                                        avg_salary_non_tenured[new_list[5][0:4]] = float(new_list[4])
                                        avg_salary_counter_non_tenured[new_list[5][0:4]] = 1
                        except ValueError:
                            break
            new_list = []
            count += 1
        if boolean:

            # sorts the tenured dictionary by year and reassigns values
            for year in sorted(avg_salary_tenured.keys()):
                sorted_tenured_dict[year] = avg_salary_tenured[year]

            # finds the average salary each year for tenured staff
            for year in sorted_tenured_dict.keys():
                sorted_tenured_dict[year] = avg_salary_tenured[year] / avg_salary_counter_tenured[year]
            return sorted_tenured_dict
        else:

            # sorts the non-tenured dictionary by year and reassigns values
            for year in sorted(avg_salary_non_tenured.keys()):
                sorted_non_tenured_dict[year] = avg_salary_non_tenured[year]

            # finds the average salary each year for non-tenured staff
            for year in sorted_non_tenured_dict.keys():
                sorted_non_tenured_dict[year] = avg_salary_non_tenured[year] / avg_salary_counter_non_tenured[year]
            return sorted_non_tenured_dict


def correlate_data(tenured_dict, non_tenured_dict):
    """
    takes a tenured and non-tenured dictionary and correlates the average salary values for each year in each dictionary

    :param tenured_dict: (dict) a dict in the style created by tenure_salary_change
    :param non_tenured_dict: (dict) a dict in the style created by tenure_salary_change
    :return: (list) a list of correlated data
    """
    new_list = []
    correlated_data = []

    # checks if the dates match in the data, and if they do, combines the data into a list of two items
    for key in non_tenured_dict.keys():
        if key in tenured_dict.keys():
            new_list.append(round(tenured_dict[key], 2))
            new_list.append(round(non_tenured_dict[key], 2))
            correlated_data.append(new_list)
        new_list = []
    return correlated_data


def line_plot_salary(data, tenure, label, done):
    """
    makes a line plot of the average salaries of tenured and non-tenured professors from the years 2011-2022

    :param data: (list) a list of data created by correlate_data
    :param tenure: (int) either a 1 or 0, used to determine which data is plotted, tenured or non-tenured
    :param label: (str) a str of the label for each line
    :param done: (bool) a bool used to determine if the function is done plotting
    :return: a plot of the data
    """
    # sets the y values as the selected data, x values as the years 2011-2022
    y_values = [entry[tenure] for entry in data]
    x_values = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    plt.plot(x_values, y_values, label=label)
    if done:

        # checks if all data is done being processed before adding the x label, y label, title, and legend
        plt.xlabel("Years")
        plt.ylabel("Average Salary")
        plt.title("Tenured vs Non Tenured Salary")
        plt.legend()
        plt.show()


def main():
    """
    makes all three graphs and visualizations

    :return: graphs of visualizations
    """
    # plots the bar graph of the average salary from each school
    avg_salary_bar_graph_schools(school_salaries("higher_ed_employee_salaries.csv"))

    # plots the bar graph of the average salary from each department
    avg_salary_bar_graph_dept(dept_salaries("higher_ed_employee_salaries.csv"))

    # first plots tenured data as a line plot, then plots non-tenured data
    line_plot_salary(correlate_data(tenure_salary_change("higher_ed_employee_salaries.csv", True),
                                    tenure_salary_change("higher_ed_employee_salaries.csv", False)), 0, "Tenured",
                     False)
    line_plot_salary(correlate_data(tenure_salary_change("higher_ed_employee_salaries.csv", True),
                                    tenure_salary_change("higher_ed_employee_salaries.csv", False)), 1, "Non-Tenured",
                     True)


main()
