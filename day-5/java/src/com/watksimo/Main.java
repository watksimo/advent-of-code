package com.watksimo;
import java.util.ArrayList;
import java.util.Collections;

public class Main
{

    public static void main(String[] args) {
        SeatList partOne = new SeatList(new String[]{"BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"});
        System.out.printf("Part 1: Maximum seat number is %d%n", partOne.getMaxSeatNumber());
    }
}

class SeatList {

    ArrayList<Integer> SeatList;

    public SeatList(String[] codeList) {
        this.SeatList = new ArrayList<>(codeList.length);
        for(int i=0; i<codeList.length; i++) {
            int seatNum = this.getSeatFromCode(codeList[i]);
            this.SeatList.add(seatNum);
        }
    }

    public int getMaxSeatNumber() {
        return Collections.max(this.SeatList);
    }

    public ArrayList<Integer> getSeatList() {
        return this.SeatList;
    }

    private int getSeatID(int row, int column) {
        return(row * 8 + column);
    }

    private String[] separateCode(String inputCode) {
        int lPos = inputCode.indexOf('L');
        int rPos = inputCode.indexOf('R');
        int colStart;

        if (lPos < 0 || (rPos < lPos && rPos > 0)) {
            colStart = rPos;
        } else {
            colStart = lPos;
        }
        return new String[]{inputCode.substring(0, colStart), inputCode.substring(colStart, inputCode.length())};
    }

    private int get_code_value(String inputCode) throws Exception {
        double min_val = 0;
        double max_val = (int)Math.pow(2, inputCode.length()) - 1;

        for(int i = 0; i < inputCode.length(); i++) {
            char codeChar = inputCode.charAt(i);
            double mid_diff_val = (max_val - min_val) / 2.0;
            if(codeChar == 'F' || codeChar == 'L') {  // Lower half
                max_val = (double)Math.floor(max_val - mid_diff_val);
            }
            if(codeChar == 'B' || codeChar == 'R') {  // Upper half
                min_val = (double)Math.ceil(max_val - mid_diff_val);
            }
        }

        if(min_val == max_val) {
            return (int)min_val;
        }

        throw new Exception("Code conversion did not converge to a single seat.");
    }

    private int getSeatFromCode(String inputCode) {
        String[] sepCodes = this.separateCode(inputCode);
        try {
            int rowNum = this.get_code_value(sepCodes[0]);
            int colNum = this.get_code_value(sepCodes[1]);
            return this.getSeatID(rowNum, colNum);
        } catch (Exception e) {
            System.err.println(e);
            return -1;
        }

    }

}
