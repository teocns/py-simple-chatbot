import easygui
import os.path
import random
from os import path
import pandas as pd



def chatHandle(userInput, csv_columns, csv_rows,requestName):
    greetings = ['hola', 'hello', 'hi', 'hi', 'hey!', 'hey']

    formatted_input = userInput.lower().replace("?","")

    

    # format csv columns to lower
    csv_columns = (map(lambda x: x.lower().strip(),csv_columns))
    
    column_index = -1


    formatted_input_parts = formatted_input.split(' ')
    for column in csv_columns:
        column_index+=1
        column_name_parts = column.lower().split(' ')
        for part in formatted_input_parts:
            if part in column_name_parts:
                # User wants to know some data about someone in the excel. Let's see if we can find what/who is the user looking for

                data_row_index = 0
                for row in csv_rows:
                    
                    data_cell_index = -1
                    for data_cell in row:
                        data_cell_index += 1

                        # check if any parts of the input is in this cell value
                    
                        if (str(data_cell).lower().strip() == requestName):
                            # User definitely wants to know another column value of this row, so let's get it 
                            return "Your "+column+" is "+ ( str(row[column_index+1]) )

                
    # If we got here, we didn't find anything in the excel that the user was specifically searching for. Let's talk with him!
    greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
    random_greeting = random.choice(greetings)

    question = ['How are you?','How are you doing?']
    responses = ['Okay',"I'm fine"]
    random_response = random.choice(responses)
    if userInput in greetings:
        return (random_greeting)
    elif userInput in question:
        return (random_response)
    else:
        return "Sorry, I didn't understand that. Try asking for something else!"


while easygui.ccbox(
    "I will now ask you to choose a .xls or .xlsx file",
    "Chatbot"):

    filename1 = easygui.fileopenbox()

    # try:
    if path.exists(filename1):

        # Read Excel File
        excel_data_df = pd.read_excel(filename1, sheet_name="Sheet1")

        # Get all Excel available columns
        columns = excel_data_df.columns.ravel()

        # Get all Names
        all_names =  map(lambda x: x[1].lower().strip(), excel_data_df.itertuples())
        # Read user Input
        while True:
            selected_name = easygui.enterbox('What is your name?', title='Chatbot', default='', strip=True).lower().strip()
            if selected_name in all_names:
                while True:

                    all_columns_string = ""
                    for col in columns:
                        all_columns_string += col + ", "
                    all_columns_string = all_columns_string[0 : len(all_columns_string)-2]

                    user_input = easygui.enterbox(msg='Hey '+selected_name.capitalize()+', this is what I know about you:\n'+all_columns_string+'\nAsk me and you will see!', title='Chatbot', default='', strip=True)
                    if user_input:
                        easygui.msgbox(chatHandle(user_input, columns, excel_data_df.itertuples(),selected_name),title="Chatbot")
                    else:
                        exit()
            easygui.msgbox('Sorry, but I couldn\'t find anybody named '+selected_name+' in the list.',title="Chatbot")
            

    else:
        raise ValueError('A very specific bad thing happened.')
    # except:
    easygui.msgbox(
        "We couldn't read your stylesheet! Please select a valid excel file.", title="Chatbot")


