#!/usr/bin/env python
# coding: utf-8

# # Written Report

# In[ ]:


# Ted said we could include our analysis up here
# Please see the written report.

# The data concludes, through various factors, that Charter schools are better academically than Distric schools; despite the District schools recieving more funding and having a larger student population. 

# 1.) The data shows that Charter schools, with a smaller student population, had all around higher test scores compared to Distric schools with a higher student population.
    # An inferance can be made that students were able to recieve more attention from their teachers and by extension were more knowledgable when taking exams.
    
    
# 2.) Even though the Charter schools had smaller Total Budgets and Student Budgets than District schools, they seemed to have allocated their resources in a way that had an educational impact on their students. 


# 3.) The Charter school's Average, Passing percentages and Overall percentage scores seemed to be fairly close in terms of scores. The District school's Average, Passing percentages and Overall percentage scores seemed to vary largely suggesting that the quality of education needs to be improved to see more consistent test results from students.


# In[141]:


import pandas as pd
from pathlib import Path

# File to Load
# It used to be run from the schools_complete.csv and students_complete.csv but I put it in a Resources folder in case. If there's issues run it just as I did (schools_complete.csv and students_complete.csv)
school_information = Path("C:/Users/evanm/OneDrive/Desktop/PyCitySchools/Resources/schools_complete.csv")
student_information = Path("C:/Users/evanm/OneDrive/Desktop/PyCitySchools/Resources/students_complete.csv")

# Read data file and store into Pandas DataFrames
school_data = pd.read_csv(school_information)
student_data = pd.read_csv(student_information)

# Merge data into a single dataset.  
school_info_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_info_complete.head()


# In[ ]:





# # Distric Summary

# In[142]:


# The total number of unique schools
# Ted taught us this during office hours on 7/24/23
#school_count =pd.DataFrame(school_data_complete).nunique(axis = 0)
#school_names.value_counts("school_name")


# In[143]:


# Ted taught us this during office hours on 7/24/23
# school_count = school_data.count(axis = 0)
# scool_count = school_data_complete["School ID"].count()
school_count = pd.DataFrame(school_info_complete).nunique(axis = 0)
school_count = school_count["School ID"]
school_count


# In[144]:


# The Total number of students
student_counter = pd.DataFrame(school_info_complete).nunique(axis = 0)
student_counter = student_counter["Student ID"]
student_counter


# In[145]:


# The total budget
#total_budget["budget"].sum()
total_budget = pd.DataFrame(school_data).sum(axis = 0)
total_budget = total_budget["budget"]
total_budget


# In[146]:


# The Average math score (mean)
#average_math_score["math_score"].mean()
average_math_score = pd.DataFrame(school_info_complete).mean(axis = 0)
average_math_score = average_math_score["math_score"]
average_math_score


# In[147]:


# The Average reading score (mean)
average_reading_score = pd.DataFrame(school_info_complete).mean(axis = 0)
average_reading_score = average_reading_score["reading_score"]
average_reading_score


# In[148]:


# Percentage passing math (the percentage of students who passed math) (math scores greather than or equal to 70))
passing_math_count = school_info_complete[(school_info_complete["math_score"] >= 70)].count()
passing_math_percentage = passing_math_count / float(student_counter) * 100
passing_math_percentage = passing_math_percentage["math_score"]
passing_math_percentage


# In[149]:


# Percentage passing reading (the percentage of students who passed reading) (hint: look at how the math percentage was calculated)  
passing_reading_count = school_info_complete[(school_info_complete["reading_score"] >= 70)].count()
passing_reading_percentage = passing_reading_count / float(student_counter) * 100
passing_reading_percentage = passing_reading_percentage["reading_score"]
passing_reading_percentage


# In[150]:


# Percentage overall passing (the percentage of students who passed math AND reading)
passing_math_reading_count = school_info_complete[
    (school_info_complete["math_score"] >= 70) & (school_info_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count / float(student_counter) * 100
overall_passing_rate


# In[151]:


# Create a high-level snapshot of the district's key metrics in a DataFrame
# Seperating code like this becuase all together I was getting errors
district_summary = pd.DataFrame({
    
    "Total Schools": [school_count],
    "Total Students": [student_counter],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math_score],
    "Average Reading Score": [average_reading_score],
    "% Passing Math": [passing_math_percentage],
    "% Passing Reading":[passing_reading_percentage],
    "Overall Passing Rate": [overall_passing_rate]
    
                                    })



# In[152]:


# Formatting
district_summary["Total Schools"] = district_summary["Total Schools"].map("{:,}".format)
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)
district_summary["Average Math Score"] = district_summary["Average Math Score"].map("{:,}".format)
district_summary["Average Reading Score"] = district_summary["Average Reading Score"].map("{:,}".format)
district_summary["% Passing Math"] = district_summary["% Passing Math"].map("{:,}".format)
district_summary["% Passing Reading"] = district_summary["% Passing Reading"].map("{:,}".format)
district_summary["Overall Passing Rate"] = district_summary["Overall Passing Rate"].map("{:,}".format)


# In[153]:


# Display the DataFrame
district_summary


# # School Summary

# In[154]:


# Decided to throw this up here so I didn't have to use groupy by all the time
# Groupby is used for grouping the data according to the categories and applying a function to the categories. It also helps to aggregate data efficiently. The Pandas groupby() is a very powerful function with a lot of variations. It makes the task of splitting the Dataframe over some criteria really easy and efficient.
each_school = school_info_complete.groupby(['school_name'])


# In[155]:


# Use the code provided to select all of the school types
school_types = school_data.set_index('school_name')['type']
school_types


# In[156]:


# Calculate the total student count per school
# per_school_counts = pd.DataFrame(school_info_complete)
# per_school_counts.value_counts("school_name") #.sum()
per_school_counts = school_info_complete["school_name"].value_counts()
per_school_counts


# In[157]:


# Calculate the total school budget per capita (per student) spending per school
per_school_budget = school_data.set_index(["school_name"])["budget"]
per_school_budget



# In[158]:


per_school_capita = per_school_budget/per_school_counts
per_school_capita


# In[159]:


# Calculate the average test scores per school
per_school_math = each_school["math_score"].mean()
per_school_math



# In[160]:


per_school_reading = each_school["reading_score"].mean()
per_school_reading


# In[161]:


# Calculate the number of students per school with math scores of 70 or higher
students_passing_math = school_info_complete[school_info_complete["math_score"]>=70].groupby(["school_name"]).size()
# students_passing_math
school_students_passing_math = (students_passing_math/per_school_counts)*100
school_students_passing_math


# In[162]:


# Calculate the number of students per school with reading scores of 70 or higher
students_passing_reading = school_info_complete[school_info_complete["reading_score"]>=70].groupby(["school_name"]).size()
school_students_passing_reading = (students_passing_reading/per_school_counts)*100
school_students_passing_reading


# In[163]:


# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = school_info_complete[
    (school_info_complete["reading_score"] >= 70) & (school_info_complete["math_score"] >= 70)]

school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()

school_students_passing_math_and_reading


# In[164]:


# Use the provided code to calculate the passing rates
# Don't use this for calculations
per_school_passing_math = school_students_passing_math / per_school_counts * 100
per_school_passing_reading = school_students_passing_reading / per_school_counts * 100
overall_passing_rate = school_students_passing_math_and_reading / per_school_counts * 100

per_school_passing_math


# In[165]:


# Don't use this for calculations
per_school_passing_reading


# In[166]:


overall_passing_rate


# In[184]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame ({

    "School Type": school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": school_students_passing_math,
    "% Passing Reading": school_students_passing_reading,
    "% Overall Passing Rate": overall_passing_rate,
    
})


# In[185]:


# Formatting
# Couldn't figure out this error with formatting and asked Ted for help. It doesn't change my answers but if it was formatted coreectly it broke some of my other code
per_school_summary["School Type"] = per_school_summary["School Type"].map("{:,.2f}".format)
per_school_summary["Total Students"] = per_school_summary["Total Students"].map("{:,.2f}".format)
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)
per_school_summary["Average Math Score"] = per_school_summary["Average Math Score"].map("{:,.2f}".format)
per_school_summary["Average Reading Score"] = per_school_summary["Average Reading Score"].map("{:,.2f}".format)
per_school_summary["% Passing Math"] = per_school_summary["% Passing Math"].map("{:,.2f}".format)
per_school_summary["% Passing Reading"] = per_school_summary["% Passing Reading"].map("{:,.2f}".format)
per_school_summary["% Overall Passing Rate"] = per_school_summary["% Overall Passing Rate"].map("{:,.2f}".format)


# In[186]:


# Display the DataFrame
per_school_summary


# In[187]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
# https://stackoverflow.com/questions/44315455/ascending-and-descending-order-in-python-3
top_schools = per_school_summary.sort_values(["% Overall Passing Rate"], ascending=False)
top_schools.head(5)


# In[188]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
# https://stackoverflow.com/questions/44315455/ascending-and-descending-order-in-python-3
bottom_schools = per_school_summary.sort_values(
    ["% Overall Passing Rate"], ascending=True)
bottom_schools.head(5)


# In[189]:


# Use the code provided to separate the data by grade
ninth_graders = school_info_complete[(school_info_complete["grade"] == "9th")]
tenth_graders = school_info_complete[(school_info_complete["grade"] == "10th")]
eleventh_graders = school_info_complete[(school_info_complete["grade"] == "11th")]
twelfth_graders = school_info_complete[(school_info_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grader_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
tenth_grader_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_grader_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
twelfth_grader_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame(
    {
        "9th": ninth_grader_math_scores,
        "10th": tenth_grader_math_scores,
        "11th": eleventh_grader_math_scores,
        "12th": twelfth_grader_math_scores,
    }
)
     # Minor data wrangling
math_scores_by_grade.index.name = None

 # Display the DataFrame
math_scores_by_grade


# In[190]:


# Use the code provided to separate the data by grade
ninth_graders = school_info_complete[(school_info_complete["grade"] == "9th")]
tenth_graders = school_info_complete[(school_info_complete["grade"] == "10th")]
eleventh_graders = school_info_complete[(school_info_complete["grade"] == "11th")]
twelfth_graders = school_info_complete[(school_info_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the the `reading_score` column for each.
ninth_grader_reading_scores = school_info_complete[(school_info_complete["grade"]=="9th")].groupby("school_name")["reading_score"].mean()
tenth_grader_reading_scores = school_info_complete[(school_info_complete["grade"]=="10th")].groupby("school_name")["reading_score"].mean()
eleventh_grader_reading_scores = school_info_complete[(school_info_complete["grade"]=="11th")].groupby("school_name")["reading_score"].mean()
twelfth_grader_reading_scores = school_info_complete[(school_info_complete["grade"]=="12th")].groupby("school_name")["reading_score"].mean()

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({
    
        "9th": ninth_grader_reading_scores,
        "10th": tenth_grader_reading_scores,
        "11th": eleventh_grader_reading_scores,
        "12th": twelfth_grader_reading_scores,
    
                            })

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th","10th","11th","12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# In[191]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[192]:


# https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/
# I read online I could use .describe() to help balance out an error I was having with pd.cut. Something about making a numerical value instead of a string or series
per_school_capita.describe()


# In[193]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()


# In[194]:


# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels)

school_spending_df


# In[195]:


#  Calculate averages for the desired columns. 

                            
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing Rate"].mean()
 


# In[196]:


# Assemble into DataFrame
spending_summary =  pd.DataFrame({
    
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing Rate": overall_passing_spending

})
    



# Display results
spending_summary 


# In[197]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[198]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], size_bins, labels)
per_school_summary


# In[199]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Overall Passing Rate"].mean()


# In[200]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = pd.DataFrame(
    {
        "Average Math Score": size_math_scores,
        "Average Reading Score": size_reading_scores,
        "% Passing Math": size_passing_math,
        "% Passing Reading": size_passing_reading,
        "% Overall Passing Rate": size_overall_passing,
    }
)

# Display results
size_summary


# In[201]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing Rate"].mean()


# In[202]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame (
                            {
          "Average Math Score" : average_math_score_by_type,
          "Average Reading Score": average_reading_score_by_type,
          "% Passing Math": average_percent_passing_math_by_type,
          "% Passing Reading": average_percent_passing_reading_by_type,
          "% Overall Passing Rate": average_percent_overall_passing_by_type

})

# Display results
type_summary


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




