(ns nltk.core
  (:use [net.cgrand.enlive-html])
  (:require [clj-time.core :as time])
  (:require [clj-time.format :as f])
  (:require [clojure.data.json :as json])
  (:require [clojure.java.io :as io]))

(comment
  "wget http://publications.europa.eu/code/en/en-5000500.htm")

(defn fetch-page
  [file-path]
  (html-resource
   (java.io.StringReader. (slurp file-path))))

(defn extract-rows [page]
  (select page [:table#listOfCountriesTable :tr]))

(defn extract-content [cols]
  {:country (clojure.string/replace (re-find #"[^()]+" (nth cols 0)) #"&nbsp;" "") 
   :nationality (first (select (nth cols 5) [text-node])) })

(defn extract-columns [row]
  (select row [:td]))

(comment (take 110
               (->> (fetch-page "en-5000500.htm")
                    extract-rows
                    (drop 1)
                    (map extract-columns)
                    (remove #(< (count %) 9))
                    (map #(-> { :all (first (select (nth % 5) [text-node]))})))))

(defn countries-nationalities []
  (->> (fetch-page "en-5000500.htm")
       extract-rows
       (drop 1)
       (map extract-columns)
       (remove #(< (count %) 9))
       (concat [{:country "England" :nationality "English"}])
       (concat [{:country "Wales" :nationality "Welsh"}])
       (concat [{:country "Scotland" :nationality "Scottish"}])
       (concat [{:country "Northern Ireland" :nationality "Northern Irish"}])))

(defn write-to-file [rows file]
  (spit file (json/write-str rows)))
