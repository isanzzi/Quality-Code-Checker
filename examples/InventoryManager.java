public class InventoryManager {
    
    // Test case for: Multiple violations in one file
    
    // TooManyParameters: 7 parameters
    public Product addProduct(String name, String sku, double price, int quantity, 
                             String category, String supplier, String warehouse) {
        Product product = new Product();
        product.setName(name);
        product.setSku(sku);
        product.setPrice(price);
        product.setQuantity(quantity);
        product.setCategory(category);
        product.setSupplier(supplier);
        product.setWarehouse(warehouse);
        return product;
    }
    
    // DeepNesting: 5 levels
    public void updateStock(String productId, int quantity) {
        Product product = findProduct(productId);
        if (product != null) {
            if (quantity > 0) {
                if (product.getQuantity() >= 0) {
                    if (isWarehouseAvailable(product.getWarehouse())) {
                        if (hasPermission("UPDATE_STOCK")) {
                            product.setQuantity(product.getQuantity() + quantity);
                            save(product);
                        }
                    }
                }
            }
        }
    }
    
    // TooManyVariables: 11 local variables
    public StockReport generateReport(String warehouseId, Date startDate, Date endDate) {
        StockReport report = new StockReport();
        List<Product> products = getProductsByWarehouse(warehouseId);
        int totalProducts = products.size();
        int lowStockCount = 0;
        int outOfStockCount = 0;
        double totalValue = 0.0;
        Map<String, Integer> categoryCount = new HashMap<>();
        List<Product> lowStockProducts = new ArrayList<>();
        List<Product> outOfStockProducts = new ArrayList<>();
        Date reportDate = new Date();
        String reportId = generateReportId();
        
        for (Product p : products) {
            if (p.getQuantity() == 0) outOfStockCount++;
            if (p.getQuantity() < 10) lowStockCount++;
            totalValue += p.getPrice() * p.getQuantity();
        }
        
        report.setTotalProducts(totalProducts);
        report.setLowStockCount(lowStockCount);
        report.setTotalValue(totalValue);
        
        return report;
    }
    
    // VariableNameTooShort: multiple short variables
    public void quickCheck(String id) {
        Product p = findProduct(id);
        int q = p.getQuantity();
        double pr = p.getPrice();
        String c = p.getCategory();
        String w = p.getWarehouse();
        boolean ok = q > 0 && pr > 0;
        
        if (ok) {
            System.out.println("Product OK");
        }
    }
    
    // TooManyMethodCalls: 8 method calls
    public void processOrder(Order order) {
        validate(order);
        checkStock(order);
        reserve(order);
        calculateTotal(order);
        applyDiscount(order);
        processPayment(order);
        updateInventory(order);
        sendConfirmation(order);
        logOrder(order);
    }
    
    private Product findProduct(String id) { return null; }
    private boolean isWarehouseAvailable(String warehouse) { return true; }
    private boolean hasPermission(String perm) { return true; }
    private void save(Product p) {}
    private List<Product> getProductsByWarehouse(String id) { return null; }
    private String generateReportId() { return ""; }
    private void validate(Order o) {}
    private void checkStock(Order o) {}
    private void reserve(Order o) {}
    private void calculateTotal(Order o) {}
    private void applyDiscount(Order o) {}
    private void processPayment(Order o) {}
    private void updateInventory(Order o) {}
    private void sendConfirmation(Order o) {}
    private void logOrder(Order o) {}
}
