package main;

public class Student {

private double GPA;
private int SAT;
private int ACT;
private int NumfAc;


  public Student(double GPA, int SAT, int ACT, int NumfAc) {
    this.GPA = GPA;
    this.SAT = SAT;
    this.ACT = ACT;
    this.NumfAc = NumfAc;
  }

  public double getGPA() {
    return this.GPA;
  }

  public int getSAT() {
    return this.SAT;
  }

  public int getACT() {
    return this.ACT;
  }

  public int getNumfAc() {
    return this.NumfAc;
  }

}
