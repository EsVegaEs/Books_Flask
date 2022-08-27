CREATE SCHEMA IF NOT EXISTS `booksandusers` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `booksandusers` ;

-- -----------------------------------------------------
-- Table `booksandusers`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksandusers`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `booksandusers`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksandusers`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `page_number` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `booksandusers`.`favbooks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `booksandusers`.`favbooks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favbooks_authors_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_favbooks_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_favbooks_authors`
    FOREIGN KEY (`author_id`)
    REFERENCES `booksandusers`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favbooks_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `booksandusers`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
