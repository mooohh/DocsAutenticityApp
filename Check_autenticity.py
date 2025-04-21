import hashlib





def caculate_hash(file_, hash_type="sha256"):
    """
    Calculate the SHA-256 hash of a file.
    
    :param file_path: Path to the file
    :return: SHA-256 hash of the file
    """
    
    hash_func = hashlib.new(hash_type)
    
    
    while chunk := file_.read(4096):
            hash_func.update(chunk)
            
    # Convertit le hash en une chaîne de caractères hexadécimale (donc lisible).    
    return hash_func.hexdigest()


def check_docs_authenticity(intial_file, file_to_be_verified, hash_type="sha256"):
    
    """
    Check the integrity of a file by comparing its hash with the original file's hash.
    
    :param intial_file: Path to the original file
    :param file_to_be_verified: Path to the file to be verified
    :param hash_type: Type of hash to use (default is SHA-256)
    :return: True if the hashes match, False otherwise
    """
    
    # Calculate the hash of the original file
    intial_file_hash = caculate_hash(intial_file, hash_type)
    
    # Calculate the hash of the file to be verified
    file_to_be_verified_hash = caculate_hash(file_to_be_verified, hash_type)
    
    # Compare the hashes
    return intial_file_hash == file_to_be_verified_hash



