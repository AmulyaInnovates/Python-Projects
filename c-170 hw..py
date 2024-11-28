import tkinter as tk

class Grade3:
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
    
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100 / 200
        percentage_grade_3_label.config(text=f"Percentage for Grade 3: {grade_3_percentage}%")
        

class Grade5:
    def __init__(self, language_arts, mathematics, social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
    
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100 / 300
        percentage_grade_5_label.config(text=f"Percentage for Grade 5: {grade_5_percentage}%")
        

class Grade10:
    def __init__(self, language_arts, mathematics, social_studies, foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
    
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100 / 400
        percentage_grade_10_label.config(text=f"Percentage for Grade 10: {grade_10_percentage}%")

root = tk.Tk()
root.geometry("400x300")
root.title("Grade Percentage Calculator")

percentage_grade_3_label = tk.Label(root, text="")
percentage_grade_3_label.pack(pady=10)

percentage_grade_5_label = tk.Label(root, text="")
percentage_grade_5_label.pack(pady=10)

percentage_grade_10_label = tk.Label(root, text="")
percentage_grade_10_label.pack(pady=10)

object_grade_3 = Grade3(85, 90)
grade_3_button = tk.Button(root, text="Grade 3", command=object_grade_3.percentage)
grade_3_button.pack(padx=10, pady=10)

object_grade_5 = Grade5(85, 90, 95)
grade_5_button = tk.Button(root, text="Grade 5", command=object_grade_5.percentage)
grade_5_button.pack(padx=10, pady=10)

object_grade_10 = Grade10(85, 90, 95, 80)
grade_10_button = tk.Button(root, text="Grade 10", command=object_grade_10.percentage)
grade_10_button.pack(padx=10, pady=10)

root.mainloop()
