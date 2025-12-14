public class NotificationService {
    
    // Good code - minimal violations
    // Should only trigger VariableNameTooShort if any
    
    public void sendEmail(String recipient, String subject, String body) {
        EmailMessage message = new EmailMessage();
        message.setRecipient(recipient);
        message.setSubject(subject);
        message.setBody(body);
        
        EmailClient client = getEmailClient();
        client.send(message);
    }
    
    public void sendSms(String phoneNumber, String messageText) {
        SmsMessage sms = new SmsMessage();
        sms.setPhoneNumber(phoneNumber);
        sms.setText(messageText);
        
        SmsClient client = getSmsClient();
        client.send(sms);
    }
    
    public void sendPushNotification(String userId, String title, String content) {
        PushNotification notification = new PushNotification();
        notification.setUserId(userId);
        notification.setTitle(title);
        notification.setContent(content);
        
        PushClient client = getPushClient();
        client.send(notification);
    }
    
    private EmailClient getEmailClient() { return null; }
    private SmsClient getSmsClient() { return null; }
    private PushClient getPushClient() { return null; }
}
