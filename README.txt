The directory contains:
1. An Organizer.py file
2. A test.py directory, which contains 7 test.py files for each function in Organizer.py.

Organizer.py
    It is a data organizer for getting information from two groups of data (pre/ pro-operation). 

    The Organizer.py file contains a series of functions which can print out simple metrics. 
    By running Organizer.py, simple metrics will be displayed on the terminal window.

    By giving parameters to function, the user can get statistical statements for the different indicators:
    
    ------------------------------------------------------------------------------------------------------
    makeData(record_num, status)                    param record_num: int
                                                    param status: str, { "PREOP", "POSTOP" }

    Retrieve data from txt, calculate lateral distance and height, return a list contains patient's status, 
    id, age, gender, lateral distance, and height
    ------------------------------------------------------------------------------------------------------
    printAvg(pre_data, post_data, direction)    param pre_data, post_data: 2-dimensional list of patient data, 
                                                each tuple in the list is created by makeData() function.
                                                param direction: str, { "lateral", "height" }

    Print the average performance(direction) among pre, post-operation status
    ------------------------------------------------------------------------------------------------------
    printShortest(pre_data, post_data, direction):      param pre_data, post_data: 2-dimensional list of 
                                                        patient data, each tuple in the list is created by 
                                                        makeData() function. 
                                                        param direction: str, { "lateral", "height" }

    Print the shortest performance(direction) among pre, post-operation status
    ------------------------------------------------------------------------------------------------------
    printLongest(pre_data, post_data, direction):       param pre_data, post_data: 2-dimensional list of 
                                                        patient data, each tuple in the list is created by 
                                                        makeData() function.
                                                        param direction: str, { "lateral", "height" }
    Print the highest/longest performance(direction) among pre, post-operation status
    ------------------------------------------------------------------------------------------------------
    printHighest(pre_data, post_data, gender, direction):   param pre_data, post_data: 2-dimensional list of 
                                                            patient data, each tuple in the list is created 
                                                            by makeData() function.
                                                            param gender: str, { "female", "male" }
                                                            param direction: str, { "lateral", "height" }
    Print the highest/longest performance(direction) among pre, post-operation status referred to gender
    ------------------------------------------------------------------------------------------------------
    printSortBy(dataList, sortedOn, reverse):       param dataList: 2-dimensional list of patient data, 
                                                    each tuple in the list is created by makeData() function.
                                                    param sorted_item: list of feature with 2 features, 
                                                    { [ "age", "lateral" ] , ["age", "height"]...etc }
                                                    param reverse: boolean, { False: "ascending ", True: "descending" }
    Print the data sorted on indicated features by ascending or descending
    ------------------------------------------------------------------------------------------------------
    
In the Organizer.py file, 
    the dictionary of the number keys and the string values are provided, which is only for avoiding typo issues. 
    The user can give the string value to function as the parameters directly.

    Test.py contains 7 Test*.py files and needed testing file.txt. Each test case is created by subclassing unittest.TestCase.

    In the test.py directory, the User can execute all Test*.py at once by running:
    >> python -m unittest Test*.py
