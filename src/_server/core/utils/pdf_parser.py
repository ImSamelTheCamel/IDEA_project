
import pdfplumber
from .text_processor import Text_Processor

class PDF_parser:
    def __init__(self, pdf):
        self.pdf = pdf
        self.text_processor = None

    @classmethod
    def create_instance(cls, pdf_path):                         #validate that a pdf is valid before creating an instance of the class
        try:                                            
            with pdfplumber.open(pdf_path) as file:
                pass            
            return cls(pdf_path)
        except Exception as e:
                print(f"Error: '{pdf_path}' is not a valid PDF.")
                return None

    def convert_pdf(self):
        if self.pdf is None:
            return "No valid pdf"
        with pdfplumber.open(self.pdf) as pdf_file:
            raw_text = ""
            for page in pdf_file.pages:
                raw_text += page.extract_text()
            pdf_file.close()
        self.text_processor = Text_Processor(raw_text)
        processed_text = self.text_processor.process_text()
        return processed_text

    def get_class(self):
        return self.text_processor.get_class_name()
    
    def get_semester(self):
        return self.text_processor.get_semester()
    
    def get_class_and_semester(self):
        return self.text_processor.get_class_and_semester()
    