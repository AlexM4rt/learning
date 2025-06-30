# Write your solution here
def main():

    def user_input():
        points_exercises=[]
     
        while True:
            input_user=input("Exam points and exercises completed: ")
            x=input_user.split(" ")
            if input_user=="":
                break
            if len(x)==2:
                test_points=int(x[0])
                exercises_done=int(x[1])
                points_exercises.append((test_points,exercises_done))
            
        
        #print(points_exercises)
        return points_exercises

    def exercise_points(points_exercises):
        
        exercise_points=[]
        for _,exercises_done in points_exercises:
            #if <=exercises_done<=10:
                #exercise_points.append(1)
            if 10<=exercises_done<20:
                exercise_points.append(1)
            elif 20<=exercises_done<30:
                exercise_points.append(2)
            elif 30<=exercises_done<40:
                exercise_points.append(3)
            elif 40<=exercises_done<50:
                exercise_points.append(4)
            elif 50<=exercises_done<60:
                exercise_points.append(5)
            elif 60<=exercises_done<70:
                exercise_points.append(6)
            elif 70<=exercises_done<80:
                exercise_points.append(7)
            elif 80<=exercises_done<90:
                exercise_points.append(8)       
            elif 90<=exercises_done<100:
                exercise_points.append(9)
            elif exercises_done>=100:
                exercise_points.append(10)
        
        #print(exercise_points)
        return exercise_points
           
    
    
    
    
    def points_list(points_exercises):
        new_points_list=[]
       
        for test_points,_ in points_exercises:
            new_points_list.append(test_points)
        
        #print(new_points_list)
        return new_points_list
        
    def grades(points_exercises): 
        exercise_pts = exercise_points(points_exercises)
        test_pts = points_list(points_exercises)
        total_grade = [a + b for a, b in zip(test_pts, exercise_pts)]
        
        
        grade=[]
        for points in total_grade:
        
            if 0<=points<=14:
                grade.append(0)
            elif 15<=points<=17:
                grade.append(1)
            elif 18<=points<=20:
                grade.append(2)
            elif 21<=points<=23:
                grade.append(3)
            elif 24<=points<=27:
                grade.append(4)
            elif 28<=points<=30:
                grade.append(5)

        return grade  

    def total_points(points_exercises): 
        exercise_pts = exercise_points(points_exercises)
        test_pts = points_list(points_exercises)
        total_points1 = [a + b for a, b in zip(test_pts, exercise_pts)]
        return total_points1
        

    def pass_percentage(grade):
        passed=[]
        failed=[]
        
        for i in grade:
            if i!=0:
                passed.append(i)
            else:
                failed.append(i)
        final_grade=(len(passed)/len(grade))*100
        return final_grade
            
                    
    def grade_distribution(passed,failed):
        print(f"Grade distribution: ")
        list_notes=[5,4,3,2,1,0]
        all_grades=passed + failed

        for numbers in list_notes:
            count=all_grades.count(numbers)
            print(f"{numbers}: {'*'*count}")
    
    points_exercises = user_input()  

    grade = grades(points_exercises)
    final_grade = pass_percentage(grade)
    total_points1 = total_points(points_exercises)
    #print(total_points1)
    

    print("Statistics: ")
    print(f"Points average: {sum(total_points1)/len(grade):.1f}")
    print(f"Pass percentage: {final_grade:.1f}\n")

    passed = [g for g in grade if g != 0]
    failed = [g for g in grade if g == 0]
    
    grade1_distribution1=grade_distribution(passed, failed)





main()





    




