import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String serverAddress = "127.0.0.1"; // Server IP address
        int serverPort = 12345; // Server port
        
        try (Socket socket = new Socket(serverAddress, serverPort);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            
            System.out.println("Connected to the server.");
            
            while (true) {
                // Create a simple menu for the client
                System.out.println("Menu:");
                System.out.println("1. Send a message to the server");
                System.out.println("2. Quit");
                int choice = Integer.parseInt(reader.readLine());
                
                if (choice == 1) {
                    System.out.print("Enter a message: ");
                    String message = reader.readLine();
                    out.println(message);
                    String response = in.readLine();
                    System.out.println("Server response: " + response);
                } else if (choice == 2) {
                    System.out.println("Goodbye!");
                    break;
                } else {
                    System.out.println("Invalid choice. Try again.");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
