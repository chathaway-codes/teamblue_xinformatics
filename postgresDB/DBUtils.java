import java.io.*;
import java.sql.*;
import javax.sql.DataSource;
import org.postgresql.ds.PGSimpleDataSource;


public class DBUtils{

	// get a DataSource object that can connect to the Database (still needs username/password
	protected static DataSource getJDBCDataSource()
	{
		PGSimpleDataSource ds = new PGSimpleDataSource();
		ds.setDatabaseName("xinfo_db");

		return ds;
	}

	// get a DataSource object that can connect to the DB
	// apply a username/password at creation time.
	protected static DataSource getJDBCDataSource(String username, String password)
	{
		PGSimpleDataSource ds = (PGSimpleDataSource)getJDBCDataSource();
		ds.setUser(username);
		ds.setPassword(password);
		return ds;
	}


}
