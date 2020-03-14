package main;

public class College {

  private String name;
  private double GPALimit;
  private int SATLimit;
  private int ACTLimit;
  private int NumfAcLimit;

  public College(String name, double GPALimit, int SATLimit, int ACTLimit, int NumfAc) {
    this.name = name;
    this.GPALimit = GPALimit;
    this.SATLimit = SATLimit;
    this.ACTLimit = ACTLimit;
    this.NumfAcLimit = NumfAcLimit;
  }

  public String getName() {
    return this.name;
  }
  
  public boolean isAccepted(Student student) {
    if (student.getGPA() < this.GPALimit) {
      return false;
    }

    if (student.getSAT() < this.SATLimit) {
      return false;
    }

    if (student.getACT() < this.ACTLimit) {
      return false;
    }

    if (student.getNumfAc() < this.NumfAcLimit) {
      return false;
    }
    return true;

  }

}
