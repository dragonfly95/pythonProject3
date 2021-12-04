
-- 테이블 board_db.customer 구조 내보내기
CREATE TABLE IF NOT EXISTS `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` int DEFAULT NULL,
  `region` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `인덱스 1` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT INTO `customer` (`id`, `name`, `category`, `region`) VALUES
	(1, '홍길동', 1, '서울'),
	(2, '강감찬', 2, '경기도'),
	(3, '김세라', 3, '인천');
