
// let testArray = new Uint8Array([0,255,2,31]);
// testArray[1] = 313;

// console.log(testArray);


// symmetric encryption 
// AES -- Advanced Encryption Standard

const crypto = require('crypto');

const key = crypto.randomBytes(32); // 32Bytes key 

const iv = crypto.randomBytes(16); // 16Bytes IV vector generation

// Function to Encrypt text

function encrypt(text){
    let cipher = crypto.createCipheriv('aes-256-cbc',key,iv);
    let encrypted = cipher.update(text,'utf8','hex');
    encrypted += cipher.final('hex');
    return encrypted;
}

// function to decrypt 

function decrypt(text){
    let decipher = crypto.createDecipheriv('aes-256-cbc',key,iv);
    let decrypted = decipher.update(text,'utf8','hex');
    decrypted += decipher.final('hex');
    return decrypted;
}

const textToEncrypt = 'Hello, World!';
const encryptedText = encrypt(textToEncrypt);
const decryptedText = decrypt(encryptedText);

console.log('Original Text:', textToEncrypt);
console.log('Encrypted Text:', encryptedText);
console.log('Decrypted Text:', decryptedText);