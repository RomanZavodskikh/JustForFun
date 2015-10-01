import java.io.*;

public class Main {
    public static void main (String[] args) {
        final ByteArrayOutputStream baos = new ByteArrayOutputStream();
        final DataOutputStream dos = new DataOutputStream(baos);

        try {
            dos.writeChars("DSL");
            dos.writeInt(32);
            dos.writeBoolean(true);

            dos.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }

        final byte[] result = baos.toByteArray();

        System.out.println("Hello world!");
        System.out.println(result);
    }
}
