-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema my_fridge
-- -----------------------------------------------------
-- 
-- 

-- -----------------------------------------------------
-- Schema my_fridge
--
-- 
-- 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_fridge` DEFAULT CHARACTER SET utf8 ;
USE `my_fridge` ;

-- -----------------------------------------------------
-- Table `my_fridge`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`users` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(250) NULL,
  `level` INT NULL,
  `permisions` VARCHAR(50) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`categorys`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`categorys` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`categorys` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `icon` VARCHAR(450) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`recipes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`recipes` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NULL,
  `time_cook` INT NULL,
  `level_recipe` INT NULL,
  `description` TEXT(1000) NULL,
  `preparation` TEXT(3000) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `img` VARCHAR(405) NULL,
  `user_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_recipes_categorys1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `my_fridge`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_recipes_categorys1`
    FOREIGN KEY (`category_id`)
    REFERENCES `my_fridge`.`categorys` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`ingredients`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`ingredients` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`ingredients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `icon` VARCHAR(450) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`ingrediente_receta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`ingrediente_receta` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`ingrediente_receta` (
  `ingredient_id` INT NOT NULL,
  `recipe_id` INT NOT NULL,
  `amount` VARCHAR(45) NULL,
  PRIMARY KEY (`ingredient_id`, `recipe_id`),
  INDEX `fk_ingredients_has_recipes_recipes1_idx` (`recipe_id` ASC) VISIBLE,
  INDEX `fk_ingredients_has_recipes_ingredients1_idx` (`ingredient_id` ASC) VISIBLE,
  CONSTRAINT `fk_ingredients_has_recipes_ingredients1`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `my_fridge`.`ingredients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ingredients_has_recipes_recipes1`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `my_fridge`.`recipes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`icon_category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`icon_category` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`icon_category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `route_icon` VARCHAR(80) NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`, `route_icon`, `category_id`),
  INDEX `fk_icon_category_categorys1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_icon_category_categorys1`
    FOREIGN KEY (`category_id`)
    REFERENCES `my_fridge`.`categorys` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_fridge`.`reviews`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `my_fridge`.`reviews` ;

CREATE TABLE IF NOT EXISTS `my_fridge`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `contenido` VARCHAR(255) NULL,
  `rate` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `recipe_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reviews_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_reviews_recipes1_idx` (`recipe_id` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `my_fridge`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_recipes1`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `my_fridge`.`recipes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
