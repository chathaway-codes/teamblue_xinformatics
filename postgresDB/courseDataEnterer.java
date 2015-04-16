import java.io.*;
import java.sql.*;
import javax.sql.DataSource;

public class courseDataEnterer{


	public static void main(String[] args) throws IOException{

		BufferedReader reader = new BufferedReader(new FileReader("sis_class_schedule_fall_2014_CSCI.csv"));

		String line;

		line = reader.readLine();
		//System.out.println(line);	

		BufferedReader inputReader = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("enter your postgresql username: ");
		String username = inputReader.readLine();
		System.out.println("enter your postgresql password: ");
		String password = inputReader.readLine();

		boolean parsable;

		try{
			Connection db = DBUtils.getJDBCDataSource(username, password).getConnection();

			//clear contents of the courses table.
			Statement deleteStmt = db.createStatement();
			String deleteQuery = "DELETE FROM courses";
			deleteStmt.executeUpdate(deleteQuery);			

			while((line = reader.readLine())!=null){
				String[] splitLine = line.split(",");
			
				//should change to exact number of columns
				if(splitLine.length == 18){
					
					//this is blank System.out.println(splitLine[6]);
					//System.out.println(line);
					PreparedStatement stmt = null;
					String query = "INSERT INTO courses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

					//the seventh value should be blank
					stmt = db.prepareStatement(query);
					try{
						parsable = true;
						for(int i = 0; i < 6; i++){
					
							System.out.println("i " + i + ": " + splitLine[i]);
							if((i == 1) || (i == 5))
								stmt.setInt(i+1, Integer.parseInt(splitLine[i]));
							else 
								stmt.setString(i+1, splitLine[i]);
						}
						for(int i = 7; i < splitLine.length; i++){
							System.out.println("i " + i + ": " + splitLine[i]);
							if((i == 16) || (i == 13) || (i == 14) || (i == 15))
								stmt.setInt(i, Integer.parseInt(splitLine[i]));
							else
								stmt.setString(i, splitLine[i]);
						}
					}catch(NumberFormatException e){
						parsable = false;
					}
					System.out.println(stmt);
					if(parsable)
						stmt.executeUpdate();

				}
	
			 }

		}catch(SQLException sqle){
			sqle.printStackTrace();
			return;
		}
	}

} 
