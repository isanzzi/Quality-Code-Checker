public class UserRepository {
    
    // Test case for: VariableNameTooShort
    public User findById(int id) {
        String q = "SELECT * FROM users WHERE id = ?";
        Connection c = getConnection();
        PreparedStatement s = c.prepareStatement(q);
        s.setInt(1, id);
        ResultSet r = s.executeQuery();
        
        User u = null;
        if (r.next()) {
            u = new User();
            u.setId(r.getInt("id"));
            u.setName(r.getString("name"));
        }
        return u;
    }
    
    // Test case for: TooManyVariables (should have 10+ local variables)
    public List<User> searchUsers(String name, String email, int minAge, int maxAge, String city) {
        List<User> results = new ArrayList<>();
        String query = "SELECT * FROM users WHERE 1=1";
        StringBuilder queryBuilder = new StringBuilder(query);
        List<Object> parameters = new ArrayList<>();
        int paramIndex = 1;
        boolean hasName = name != null && !name.isEmpty();
        boolean hasEmail = email != null && !email.isEmpty();
        boolean hasAgeFilter = minAge > 0 || maxAge > 0;
        boolean hasCityFilter = city != null && !city.isEmpty();
        String finalQuery = queryBuilder.toString();
        Connection connection = getConnection();
        
        try {
            PreparedStatement statement = connection.prepareStatement(finalQuery);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                User user = mapResultSetToUser(resultSet);
                results.add(user);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        return results;
    }
    
    // Test case for: TooManyMethodCalls (should have 5+ method calls)
    public void createUser(User user) {
        validate(user);
        encrypt(user.getPassword());
        normalize(user.getEmail());
        generateId(user);
        save(user);
        sendWelcomeEmail(user);
        logUserCreation(user);
    }
    
    private Connection getConnection() { return null; }
    private void validate(User user) {}
    private void encrypt(String password) {}
    private void normalize(String email) {}
    private void generateId(User user) {}
    private void save(User user) {}
    private void sendWelcomeEmail(User user) {}
    private void logUserCreation(User user) {}
    private User mapResultSetToUser(ResultSet rs) { return null; }
}
