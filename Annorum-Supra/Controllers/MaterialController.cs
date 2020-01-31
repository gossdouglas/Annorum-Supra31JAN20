using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using annorum_supra.Models;

namespace annorum_supra.Controllers
{
    public class MaterialController : Controller
    {
        private annorum_supra_cmps411Entities db = new annorum_supra_cmps411Entities();

        public ActionResult Index()
        {           
            annorum_supra_cmps411Entities entities = new annorum_supra_cmps411Entities();
            List<tbl_common_mtrl> material = entities.tbl_common_mtrl.ToList();

            //ViewBag.eventType = new SelectList(db.tbl_event_type, "eventType", "eventType");
            //ViewBag.customerCode = new SelectList(db.tbl_customers, "customerCode", "customerCode");
            return View(material.ToList());           
        }

        // GET: Material
        /*public ActionResult Index()
        {
            return View(db.tbl_common_mtrl.ToList());
        }*/

        // GET: Material/Details/5
        public ActionResult Details(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            tbl_common_mtrl tbl_common_mtrl = db.tbl_common_mtrl.Find(id);
            if (tbl_common_mtrl == null)
            {
                return HttpNotFound();
            }
            return View(tbl_common_mtrl);
        }

        // GET: Material/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Material/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "id,type,subtype")] tbl_common_mtrl tbl_common_mtrl)
        {
            if (ModelState.IsValid)
            {
                db.tbl_common_mtrl.Add(tbl_common_mtrl);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(tbl_common_mtrl);
        }

        // GET: Material/Edit/5
        public ActionResult Edit(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            tbl_common_mtrl tbl_common_mtrl = db.tbl_common_mtrl.Find(id);
            if (tbl_common_mtrl == null)
            {
                return HttpNotFound();
            }
            return View(tbl_common_mtrl);
        }

        // POST: Material/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "id,type,subtype")] tbl_common_mtrl tbl_common_mtrl)
        {
            if (ModelState.IsValid)
            {
                db.Entry(tbl_common_mtrl).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(tbl_common_mtrl);
        }

        // GET: Material/Delete/5
        public ActionResult Delete(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            tbl_common_mtrl tbl_common_mtrl = db.tbl_common_mtrl.Find(id);
            if (tbl_common_mtrl == null)
            {
                return HttpNotFound();
            }
            return View(tbl_common_mtrl);
        }

        // POST: Material/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(string id)
        {
            tbl_common_mtrl tbl_common_mtrl = db.tbl_common_mtrl.Find(id);
            db.tbl_common_mtrl.Remove(tbl_common_mtrl);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
