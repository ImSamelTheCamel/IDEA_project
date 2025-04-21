class Text_Processor:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.class_name = []
        self.semester = ""
        self.sections = ["a", "b", "c"]
        self.has_sections = False
        self.feedback_dictionary = {
            "a":"",
            "b":"",
            "c":""
        }  
        self.titles = [
            "Comments",
            "What aspects of the teaching or content of this course do you feel were especially good?",
            "What changes could be made to improve the teaching or the content on this course?"
        ]
        self.excluded_text = [                                      #text to exclude, all lower case
            "na",
            "",
            "responses",
            "qualitative report",
            "qualitative"
        ]

    #remove partial titles from the text
    def remove_titles(self, raw_text):
        titles = ["Comments -", 
            "What aspects of the",
            "teaching or content of this",
            "course do you feel were", 
            "especially good? -", 
            "What changes could be",
            "made to improve the",
            "teaching or the content on",
            "this course?",
            "© 2024 Anthology Inc."
        ]
        processed_text = ""
        lines = raw_text.split("\n")
        for line in lines:
            if (len(titles) > 0):
                if titles[0] in line:
                    line = line.replace(titles[0], "")
                    titles.pop(0)
            processed_text += line + "\n"
        return processed_text

    # get the semester from the pdf file
    def extract_semester(self, line):
        if "term" in line.lower():
            line_contents = line.split(":")
            return line_contents[1].strip()
        else:
            line_contents = line.split("|")
            return line_contents[0].strip()

    #extract the class title and cut the non-qualitative feedback
    def clean_text(self):
        clean_text = ""
        qualitative_feedback = False
        lines = self.raw_text.split("\n")
        line_index = 0
        for line in lines:
            if line_index == 0 or line_index == 6:          #the title for the class is on either the first or seventh line
                split_line = line.split(":")
                class_name = split_line[0].split("(")           #split the class name to remove the class section from the class name
                self.class_name.append(class_name[0].strip())
            if line_index == 2:
                self.semester = self.extract_semester(line)
            if "qualitative" in line.lower():
                qualitative_feedback = True
            if qualitative_feedback:
                clean_text += line + "\n"
            line_index += 1
        return clean_text

    #determine if there are sections in the text
    def is_sectioned(self, text):
        line_counter = 0
        check_val = 'course sections'
        for line in text.split("\n"):
            if check_val in line.lower():
                self.has_sections =  True
            line_counter += 1
            if line_counter == 2:
                break

    #process text if it has sections in it
    def process_sectioned(self, text):
        current_block = ["", ""]
        title_index = -1
        section = ""
        for line in text.split("\n"):
            current_block.append(line)    
            if len(current_block) > 1:        
                if current_block[1].lower() in self.sections:
                    section = current_block[1].lower()
                    current_block[1] = ""
                    if title_index <= 3:
                        if section in ["b", "c"]:                   #go back to the previous title index to add the same title across all secitons
                            title_index -= 1
                        if title_index == -1:
                            self.feedback_dictionary[section] += f"Section: {current_block[0]} \n"             #add the class section to the front of the section in the sectioned feedback
                        else:
                           self.feedback_dictionary[section] += "\n" + self.titles[title_index] + "\n"
                        title_index += 1
            if (section != "" and current_block[0].lower() not in self.excluded_text):
                self.feedback_dictionary[section] += current_block[0] + "\n"
            current_block.pop(0)
    
    #process text if it does not have sections in it
    def process_not_sectioned(self, text):
        processed_text = ""
        title_index = 0
        for line in text.splitlines():
            if line.split(' -')[0] in self.titles:
                processed_text += "\n" + self.titles[title_index] + "\n"
                title_index += 1
            elif (line.lower() not in self.excluded_text):
                processed_text += line + "\n"
        self.feedback_dictionary['a'] = processed_text

    #put all the sectioned feedback into a single string
    def construct_sectioned(self):
        sectioned_feedback = self.feedback_dictionary['a'] + self.feedback_dictionary['b'] + self.feedback_dictionary['c']
        return sectioned_feedback

    #put the 
    def construct_not_sectioned(self):
        return self.feedback_dictionary['a']

    # clean text and separate it into sections
    def process_text(self):
        cleaned_text = self.clean_text()
        self.is_sectioned(cleaned_text)
        if self.has_sections:
            titleless_text = self.remove_titles(cleaned_text)
            self.process_sectioned(titleless_text)
            processed_feedback = self.construct_sectioned()
        else:
            self.process_not_sectioned(cleaned_text)
            processed_feedback =  self.construct_not_sectioned()
        return processed_feedback
    
    #find the name of the class in the pdf
    def get_class_name(self):
        if "Summary" in self.class_name[0]:
            return self.class_name[1]
        else:
            return self.class_name[0]
    
    #return the semester
    def get_semester(self):
        return self.semester

    #return the semster an class name together in one line
    #this on should be used for creating database entry keys
    def get_class_and_semester(self):
        class_name = self.get_class_name()
        return class_name + " " + self.semester