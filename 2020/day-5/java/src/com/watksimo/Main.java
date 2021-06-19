package com.watksimo;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main
{

    public static void main(String[] args) throws IOException {
        List<String> inputValues = new ArrayList<>(Files.readAllLines(Paths.get("../real-input.txt")));
        SeatList partOne = new SeatList(inputValues);
        System.out.printf("Part 1: Maximum seat number is %d%n", partOne.getMaxSeatNumber());
        System.out.printf("Part 2: Missing seat number is %d.%n", partOne.findMissingSeat());
    }
}

class SeatList {

    List<Integer> SeatList;

    public SeatList(List<String> codeList) {
        this.SeatList = new ArrayList<>(codeList.size());
        for (String s : codeList) {
            int seatNum = this.getSeatFromCode(s);
            this.SeatList.add(seatNum);
        }
    }

    public int getMaxSeatNumber() {
        return Collections.max(this.SeatList);
    }

    public int findMissingSeat() {
        Collections.sort(this.SeatList);
        int counter = 0;
        for (int seatNumber : this.SeatList) {
            if(counter != 0 && seatNumber - this.SeatList.get(counter-1) != 1) {
                return seatNumber - 1;
            }
            counter++;
        }
        return -1;
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
        return new String[]{inputCode.substring(0, colStart), inputCode.substring(colStart)};
    }

    private int get_code_value(String inputCode) throws Exception {
        double min_val = 0;
        double max_val = (int)Math.pow(2, inputCode.length()) - 1;

        for(int i = 0; i < inputCode.length(); i++) {
            char codeChar = inputCode.charAt(i);
            double mid_diff_val = (max_val - min_val) / 2.0;
            if(codeChar == 'F' || codeChar == 'L') {  // Lower half
                max_val = Math.floor(max_val - mid_diff_val);
            }
            if(codeChar == 'B' || codeChar == 'R') {  // Upper half
                min_val = Math.ceil(max_val - mid_diff_val);
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
