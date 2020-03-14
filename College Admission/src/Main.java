package main;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    // Student akshay = new Student(3.5, 1320, 29, 1);
    College stanford = new College("Stanford", 3.8, 1450, 33, 4);
    College unc = new College("UNC", 3.6, 1350, 31, 4);
    College ncsu = new College("NCSU", 3.65, 1320, 30, 3);
    College harvard = new College("Harvard", 4.0, 1500, 36, 6);

    College[] colleges = {stanford, unc, ncsu, harvard};

    Scanner in = new Scanner(System.in);

    while (true) {
      System.out.print("GPA: ");
      double gpa = in.nextDouble();
      System.out.print("SAT: ");
      int sat = in.nextInt();
      System.out.print("ACT: ");
      int act = in.nextInt();
      System.out.print("Number Of Activities: ");
      int numfac = in.nextInt();

      Student student = new Student(gpa, sat, act, numfac);

      System.out.println("===========================================");
      for (College c: colleges) {
        System.out.println("Accepted to " + c.getName() + ": " + c.isAccepted(student));
      }
      System.out.println("===========================================");

    }

  }

}
