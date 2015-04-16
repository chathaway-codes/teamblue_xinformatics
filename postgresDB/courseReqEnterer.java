import java.io.*;
import java.sql.*;
import javax.sql.DataSource;

public class courseReqEnterer{
	public static void main(String[] args) throws IOException{

		BufferedReader reader = new BufferedReader(new FileReader("coursereqs.txt"));
		
		String line;	
			

		BufferedReader inputReader = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("enter your postgresql username: ");
		String username = inputReader.readLine();
		System.out.println("enter your postgresql password: ");
		String password = inputReader.readLine();

		try{	
			Connection db = DBUtils.getJDBCDataSource(username, password).getConnection();

			//delete the current contents of the coursereqs table
			Statement deleteStmt = db.createStatement();
			String deleteQuery = "DELETE FROM coursereqs";
			deleteStmt.executeUpdate(deleteQuery);

			while((line = reader.readLine())!=null){
				//for each line, we read the course name, and the prereqs, and place each into the 4 variables, which are then put into the database table through an insert prepared statement.

				String[] splitLine = line.split("\t");
			
				if(splitLine.length >= 1){
					

					PreparedStatement stmt = null;
					String query = "INSERT INTO coursereqs VALUES (?, ?, ?, ?)";
					stmt = db.prepareStatement(query);
		
	
					for(int i = 0; i < splitLine.length; i++){
						System.out.println("i " + i + ": " + splitLine[i]);
						stmt.setString(i+1, splitLine[i]);
					}
				
					int extraitr = splitLine.length + 1;
					while(extraitr <= 4){
						stmt.setString(extraitr, "none");
						extraitr++;
					}
					System.out.println(stmt);				
					stmt.executeUpdate();

				}
		
				System.out.println(line);
			}

		}catch(SQLException sqle){
			System.err.println("Issues with the SQL connection");
			sqle.printStackTrace();
			return;
		}

	}
}
