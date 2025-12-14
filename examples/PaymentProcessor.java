public class PaymentProcessor {
    
    // Test case for: TooManyParameters (6 parameters)
    public boolean processPayment(String userId, String cardNumber, String cvv, 
                                   double amount, String currency, String merchantId) {
        if (validateCard(cardNumber, cvv)) {
            return chargeCard(userId, amount, currency, merchantId);
        }
        return false;
    }
    
    // Test case for: DeepNesting (4+ levels)
    public void validateTransaction(Transaction transaction) {
        if (transaction != null) {
            if (transaction.getAmount() > 0) {
                if (transaction.getUser() != null) {
                    if (transaction.getUser().isActive()) {
                        if (transaction.getUser().hasValidPaymentMethod()) {
                            processTransaction(transaction);
                        }
                    }
                }
            }
        }
    }
    
    // Test case for: TooManyVariables and TooManyMethodCalls
    public Receipt generateReceipt(Transaction transaction) {
        Receipt receipt = new Receipt();
        String receiptId = generateReceiptId();
        String transactionId = transaction.getId();
        double amount = transaction.getAmount();
        double tax = calculateTax(amount);
        double fee = calculateFee(amount);
        double total = amount + tax + fee;
        String currency = transaction.getCurrency();
        Date timestamp = new Date();
        User user = transaction.getUser();
        String merchantName = getMerchantName(transaction);
        
        receipt.setId(receiptId);
        receipt.setTransactionId(transactionId);
        receipt.setAmount(amount);
        receipt.setTax(tax);
        receipt.setFee(fee);
        receipt.setTotal(total);
        receipt.setCurrency(currency);
        receipt.setTimestamp(timestamp);
        
        return receipt;
    }
    
    private boolean validateCard(String number, String cvv) { return true; }
    private boolean chargeCard(String userId, double amount, String currency, String merchantId) { return true; }
    private void processTransaction(Transaction t) {}
    private String generateReceiptId() { return ""; }
    private double calculateTax(double amount) { return 0; }
    private double calculateFee(double amount) { return 0; }
    private String getMerchantName(Transaction t) { return ""; }
}
